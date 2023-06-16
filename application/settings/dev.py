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

"""redis配置"""
# 默认缓存数据
REDIS_URL: str = "redis://:root123456@127.0.0.1:6379/0"
# 验证相关缓存
CHECK_URL: str = "redis://:root123456@127.0.0.1:6379/1"

"""mongoDB配置"""
MONGO_URI: str = "mongodb://yingming:yingming@127.0.0.1:27017/yingming"
