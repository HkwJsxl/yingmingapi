from types import ModuleType
from typing import List, Optional, Callable, Union, Dict
from importlib import import_module

from flask import Flask, Blueprint
from flask_jsonrpc import JSONRPC


class AutoBluePrint(object):
    def __init__(self, app: Optional[Flask] = None, jsonrpc: Optional[JSONRPC] = None):
        if app:
            self.init_app(app, jsonrpc)

    def init_app(self, app: Flask, jsonrpc: JSONRPC):
        """自动注册蓝图"""

        # 从配置文件中读取需要注册到项目中的蓝图路径信息
        blueprint_path_list: List = app.config.get("INSTALL_BLUEPRINTS", [])
        # 从配置文件中读取总路由模块
        url_root_path: str = app.config.get("URL_ROOT_PATH", "application.urls")
        # 总路由模块
        url_root_module: ModuleType = import_module(url_root_path)
        # 总路由列表
        if not hasattr(url_root_module, "urlpatterns"):
            message: str = "总路由文件 URL_ROOT_PATH，没有路由列表！请在总路由文件中设置 urlpatterns 路由列表"
            app.logger.error(message)
            raise Exception(message)

        root_urlpatterns: List = url_root_module.urlpatterns

        # 遍历蓝图路径列表，对每一个蓝图进行初始化
        for blueprint_path in blueprint_path_list:
            # 获取蓝图路径中最后一段的包名作为蓝图的名称
            blueprint_name: str = blueprint_path.split(".")[-1]
            # 给当前蓝图目录创建一个蓝图对象
            blueprint: Blueprint = Blueprint(blueprint_name, blueprint_path)

            # 蓝图路由的前缀
            url_prefix: str = ""

            # 蓝图下的子路由列表
            urlpatterns: List = []

            # 获取蓝图的父级目录，目的是为了拼接总路由中所有蓝图下的urls子路由文件的路径
            blueprint_father_path: str = ".".join(blueprint_path.split(".")[:-1])

            # 循环总路由列表
            for item in root_urlpatterns:
                # 判断当前蓝图是否有注册到总路由中提供对外访问，如果没有把蓝图注册到总路由中，则无法被外界访问。
                if blueprint_name in item["blueprint_url_subffix"]:
                    # 导入当前蓝图下的子路由模块
                    urls_module: ModuleType = import_module(f"{blueprint_father_path}.{item['blueprint_url_subffix']}")

                    # 获取子路由文件中的路由列表
                    urlpatterns: List = getattr(urls_module, "urlpatterns", [])
                    apipatterns: List = getattr(urls_module, "apipatterns", [])

                    # 提取蓝图路由的前缀
                    url_prefix = item["url_prefix"]
                    # 把urlpatterns的每一个路由信息添加注册到蓝图对象里面
                    for url in urlpatterns:
                        blueprint.add_url_rule(**url)

                    for api in apipatterns:
                        api["name"] = f"{url_prefix[1:].title()}.{api['rule']}"  # Home.menu
                        jsonrpc.register_view_function(**api)

                    break

            try:
                # 让蓝图自动发现模型模块
                import_module(f"{blueprint_path}.models")
            except ModuleNotFoundError:
                pass

            # 最后把蓝图对象注册到app实例对象
            # url_prefix 是地址前缀，将来我们将来实现一个总路由来声明它
            app.register_blueprint(blueprint, url_prefix=url_prefix)


# def path(rule: str, name: Union[Callable, str], **kwargs) -> Dict:
#     """绑定url地址和视图的映射关系"""
#     if isinstance(name, Callable):
#         # 子路由
#         return {"rule": rule, "view_func": name, **kwargs}
#     elif isinstance(name, str):
#         # 总路由
#         return {"url_prefix": rule, "blueprint_url_subffix": name, **kwargs}
#     else:
#         return {}


def path(rule: str, view_func: Callable, **kwargs) -> Dict:
    """绑定url地址和视图的映射关系，和参数名对应上"""
    return {"rule": rule, "view_func": view_func, **kwargs}


def include(url_prefix: str, blueprint_url_subffix: str) -> Dict:
    """
    绑定路由前缀和蓝图的映射关系（为了让总路由像Django一样注册）
    :param url_prefix: 路由前缀
    :param blueprint_url_subffix: 蓝图名称，
           格式：蓝图包名.路由模块名
           例如：蓝图目录是home, 路由模块名是urls，则参数：home.urls
    :return: Dict
    """
    return {"url_prefix": url_prefix, "blueprint_url_subffix": blueprint_url_subffix}
