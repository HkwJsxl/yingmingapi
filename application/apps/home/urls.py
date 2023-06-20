from typing import List

from application import path
from . import views, api

urlpatterns: List = [
    # path的作用就是把传递的参数转换成对应的字典结构：{"rule": "/home", "view_func": views.index, "methods": ["GET"]},
    path("/test/", views.test, methods=["GET", "POST"]),
    path("/index/", views.index),
]

# # api接口
# apipatterns = [
#     path("menu", api.menu),
# ]
# 实例化视图类，此处比较麻烦，所以你可以参考django的as_views方法，让路径和视图方法名对应。
home = api.Home()
# api接口
apipatterns = [
    path("menu", api.menu),
    path("index", home.index),
    path("list", home.list),
]
