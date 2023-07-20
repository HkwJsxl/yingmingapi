from typing import List, Dict, Any

from marshmallow import Schema, fields, validate, validates, ValidationError, decorators
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from sqlalchemy.orm import scoped_session
from flask import request

from .models import User
from application import message, db


class MobileSchema(Schema):
    """手机号唯一校验序列化器"""
    mobile: fields.String = fields.String(required=True, validate=validate.Regexp(
        regex=r"^1[3-9]\d{9}$",
        error=message.mobile_format_error
    ), error_messages={"required": message.mobile_is_required})

    @validates("mobile")
    def validate_mobile(self, mobile: str) -> str:
        """到数据库查询验证是否曾经注册过当前手机号"""
        user: User = User.query.filter(User.mobile == mobile).first()
        if user:
            raise ValidationError(message=message.mobile_is_used, field_name="mobile")
        return mobile


class UserSchema(SQLAlchemyAutoSchema):
    mobile: fields.String = auto_field(required=True, load_only=True, validates=validate.Regexp(
        regex="^1[3-9]\d{9}$",
        error=message.mobile_format_error
    ))
    password: fields.String = fields.String(required=True, load_only=True, validate=validate.Length(
        min=6,
        max=16,
        error=message.password_length_error
    ))
    re_password: fields.String = fields.String(required=True, load_only=True)
    sms_code: fields.String = fields.String(required=True, load_only=True, validate=validate.Length(
        min=4,
        max=4,
        error=message.sms_code_length_error
    ))

    class Meta:
        model: User = User
        include_fk: bool = True  # 启用外键关系
        include_relationships: bool = True  # 模型关系外部属性
        # 如果要全换全部字段，就不要声明fields或exclude字段即可
        fields: List[str] = ["id", "name", "mobile", "password", "re_password", "sms_code"]
        sqla_session: scoped_session = db.session

    @decorators.validates_schema
    def validates_schema(self, data, **kwargs) -> Dict[str, Any]:
        """全字段校验"""
        # 校验密码和确认密码
        if data["password"] != data["re_password"]:
            raise ValidationError(message=message.password_not_match, field_name="re_password")

        # todo 校验短信验证码

        data.pop("re_password")
        data.pop("sms_code")
        return data

    @decorators.post_load
    def save_object(self, data, **kwargs) -> User:
        data["name"] = data["mobile"]
        # print("request.environ---", request.environ)
        data["ip_address"] = request.environ["REMOTE_ADDR"]  # 客户端本次请求的IP地址
        user: User = User(**data)
        self.session.add(user)
        self.session.commit()
        return user
