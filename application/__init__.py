from flask import Flask


# 为了防止每次导入application都要实例化Flask对象（只有调用了init_app函数的才会实例化Flask对象）
def init_app() -> Flask:
    """用于创建app实例对象并完成初始化过程的工厂函数"""
    # 实例化flask应用对象
    app: Flask = Flask(__name__)
    return app
