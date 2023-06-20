from typing import List

from application import path
from . import views, api

urlpatterns: List = [
    # path的作用就是把传递的参数转换成对应的字典结构：{"rule": "/home", "view_func": views.index, "methods": ["GET"]},
    path("/test", views.test, methods=["GET", "POST"]),
    path("/index", views.index),
]

# apipatterns: List = [
#     path("menu", api.menu),
# ]
