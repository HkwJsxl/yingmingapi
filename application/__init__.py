from flask import Flask

from application.utils.config import Config

# 实例化配置加载类
config: Config = Config()


# 为了防止每次导入application都要实例化Flask对象（只有调用了init_app函数的才会实例化Flask对象）
def init_app(config_path: str) -> Flask:
    """用于创建app实例对象并完成初始化过程的工厂函数"""
    # 实例化flask应用对象
    app: Flask = Flask(__name__)
    # 加载配置
    config.init_app(app, config_path)

    return app
