from typing import Dict, Any

from . import serializers
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
