"""本地配置"""
# 调试模式
DEBUG: bool = True
# 语言
LANGUAGE: str = "zh_hans"
# 时区
TZ: str = "Asia/Shanghai"

"""数据库配置"""
# 数据库连接
SQLALCHEMY_DATABASE_URI: str = "mysql://yingminguser:yingming@127.0.0.1:3306/yingming?charset=utf8mb4"

# 查询时会显示原始SQL语句
SQLALCHEMY_ECHO: bool = True
