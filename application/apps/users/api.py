from typing import Dict, Any

from . import serializers, models
from application import message, code


def check_mobile(mobile: str) -> Dict[str, Any]:
    """
    验证手机号格式与是否唯一
    :param mobile: 手机号
    :return:
    """
    ms: serializers.MobileSchema = serializers.MobileSchema()
    try:
        ms.load({"mobile": mobile})
        result: Dict[str, Any] = {"error": code.CODE_OK, "errmsg": message.success}
    except serializers.ValidationError as e:
        result: Dict[str, Any] = {"error": code.CODE_VALIDATE_ERROR, "errmsg": e.message["mobile"][0]}
    return result


def register(mobile: str, password: str, re_password: str, sms_code: str) -> Dict[str, Any]:
    """
    用户信息注册
    :param mobile: 手机号
    :param password: 登录密码
    :param re_password: 确认密码
    :param sms_code: 短信验证码
    :return:
    """
    result = check_mobile(mobile)
    if result["error"] != 0:
        return result
    try:
        us: serializers.UserSchema = serializers.UserSchema()
        user: models.User = us.load({
            "mobile": mobile,
            "password": password,
            "re_password": re_password,
            "sms_code": sms_code
        })
        result: Dict[str, Any] = {"error": code.CODE_OK, "errmsg": us.dump(user)}
    except serializers.ValidationError as e:
        result: Dict[str, Any] = {"error": code.CODE_VALIDATE_ERROR, "errmsg": e.messages}
    result.headers['Access-Control-Allow-Origin'] = '*'
    result.headers['Access-Control-Allow-Method'] = 'POST'  # 如果该请求是get，把POST换成GET即可
    result.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return result
