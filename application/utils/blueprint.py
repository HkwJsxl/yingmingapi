from types import ModuleType
from typing import List, Optional, Callable
from importlib import import_module

from flask import Flask, Blueprint


class AutoBluePrint(object):
    def __init__(self, app: Optional[Flask] = None):
        if app:
            self.init_app(app)

    def init_app(self, app: Flask):
        """
        自动注册蓝图
        :param app:
        :return:
        """
        # 从配置文件中读取需要注册到项目中的蓝图路径信息
        blueprint_path_list: List = app.config.get("INSTALL_BLUEPRINTS", [])
        # 遍历蓝图路径列表，对每一个蓝图进行初始化
        for blueprint_path in blueprint_path_list:
            # 获取蓝图路径中最后一段的包名作为蓝图的名称
            blueprint_name: str = blueprint_path.split(".")[-1]
            # 给当前蓝图目录创建一个蓝图对象
            blueprint: Blueprint = Blueprint(blueprint_name, blueprint_path)

            # 导入子路由关系，blueprint_url_path就是当前蓝图下的urls模块的导包路径
            blueprint_url_path: str = blueprint_path + ".urls"
            urls_module: ModuleType = import_module(blueprint_url_path)
            urlpatterns: List = []
            try:
                urlpatterns = urls_module.urlpatterns
            except Exception:
                pass

            # 在循环中，把urlpatterns的每一个路由信息添加注册到蓝图对象里面
            for url in urlpatterns:
                blueprint.add_url_rule(**url)

            # 最后把蓝图对象注册到app实例对象
            # todo url_prefix 是地址前缀，将来我们将来实现一个总路由来声明它
            app.register_blueprint(blueprint, url_prefix="")


def path(rule: str, view_func: Callable, **kwargs):
    """绑定url地址和视图的映射关系"""
    return {"rule": rule, "view_func": view_func, **kwargs}
