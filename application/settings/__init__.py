"""公共配置"""

"""调试模式"""
DEBUG: bool = False

"""本地化国际化"""
# 语言
LANGUAGE: str = "en"
# 时区
TZ: str = "UTC"

"""数据库配置"""
# 数据库连接
SQLALCHEMY_DATABASE_URI: str = ""

# 动态追踪修改设置
SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

# 查询时会显示原始SQL语句
SQLALCHEMY_ECHO: bool = False
