from marshmallow import Schema, fields, validate, validates, ValidationError

from .models import User
from application import message


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
