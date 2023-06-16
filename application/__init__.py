from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_pymongo import PyMongo

from application.utils.config import Config

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


def init_app(config_path: str):
    """用于创建app实例对象并完成初始化过程的工厂函数"""
    app: Flask = Flask(__name__)

    # 加载配置
    config.init_config(app, config_path)
    # print("app.config---", app.config)

    # SQLAlchemy加载配置
    db.init_app(app)

    # redis加载配置
    redis_cache.init_app(app)
    redis_check.init_app(app)

    # pymongo加载配置
    mongo.init_app(app)

    return app
