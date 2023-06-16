import click, os
from typing import Optional

from flask import Flask


class Command:
    """Flask终端命令管理类"""

    def __init__(self, app: Optional[Flask] = None):
        if app:
            self.init_app(app)

    def init_app(self, app: Flask):
        self.app: Flask = app
        self.setup()

    def setup(self):
        """初始化终端命令"""
        self.blueprint()  # 自动创建蓝图目录和文件

    def blueprint(self):
        """蓝图目录生成命令"""

        @self.app.cli.command("blue")  # 指定终端命令的调用名称
        @click.option("--name", default="home", help="蓝图目录名称", type=str)
        def command(name: str):
            # os.chdir("application")  # 切换到application的apps目录下
            # os.chdir("apps")  # 切换到application的apps目录下
            os.mkdir(name)  # 生成蓝图名称对象的目录
            open("%s/__init__.py" % name, "w")
            open("%s/admin.py" % name, "w")  # adnmin后台站点配置文件
            open("%s/ws.py" % name, "w")  # websocket的视图文件
            open("%s/api.py" % name, "w")  # api接口的视图文件
            open("%s/views.py" % name, "w")  # 普通视图文件
            open("%s/models.py" % name, "w")
            open("%s/documents.py" % name, "w")
            open("%s/urls.py" % name, "w")  # 视图路由
            open("%s/test.py" % name, "w")
            open("%s/tasks.py" % name, "w")
            open("%s/serializers.py" % name, "w")  # 序列化器文件

            print("BluePrint[%s] created done...." % name)
