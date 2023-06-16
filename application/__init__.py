from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from application.utils.config import Config

# 实例化配置加载类
config: Config = Config()
# SQLAlchemy初始化
db: SQLAlchemy = SQLAlchemy()


def init_app(config_path: str):
    """用于创建app实例对象并完成初始化过程的工厂函数"""
    app: Flask = Flask(__name__)

    # 加载配置
    config.init_config(app, config_path)
    # print("app.config---", app.config)

    # SQLAlchemy加载配置
    db.init_app(app)

    return app
