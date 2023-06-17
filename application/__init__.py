from pathlib import Path

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_pymongo import PyMongo

from application.utils.config import Config
from application.utils.logger import Logger
from application.utils.commands import Command
from application.utils.blueprint import AutoBluePrint, path

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

# 终端命令管理类实例化
command: Command = Command()
# 实例化自动化蓝图类
blueprint: AutoBluePrint = AutoBluePrint()


def init_app(config_path: str) -> Flask:
    """用于创建app实例对象并完成初始化过程的工厂函数"""
    app: Flask = Flask(__name__)

    # 全局路径常量，指向项目根目录
    # Path(__file__):当前文件位置，Path()程序开始位置
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

    # 终端命令管理类加载配置
    command.init_app(app)

    # 自动化蓝图类加载配置
    blueprint.init_app(app)

    return app
