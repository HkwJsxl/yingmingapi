from pathlib import Path

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_pymongo import PyMongo

from application.utils.config import Config
from application.utils.logger import Logger

"""加载组件[单例模式]"""
# 实例化配置加载类
config: Config = Config()
# SQLAlchemy初始化
db: SQLAlchemy = SQLAlchemy()

# redis初始化
redis_cache: FlaskRedis = FlaskRedis(config_prefix="REDIS")
redis_check: FlaskRedis = FlaskRedis(config_prefix="CHECK")
# mongoDB实例化
mongo: PyMongo = PyMongo()
# 实例化日志配置类
logger: Logger = Logger()


def init_app(config_path: str) -> Flask:
    """用于创建app实例对象并完成初始化过程的工厂函数"""
    app: Flask = Flask(__name__)

    # 全局路径常量，指向项目根目录
    app.BASE_DIR: Path = Path(__file__).resolve().parent.parent

    # 加载配置
    config.init_config(app, config_path)

    # SQLAlchemy加载配置
    db.init_app(app)

    # redis加载配置
    redis_cache.init_app(app)
    redis_check.init_app(app)

    # pymongo加载配置
    mongo.init_app(app)

    # 日志加载配置
    logger.init_app(app)

    return app
