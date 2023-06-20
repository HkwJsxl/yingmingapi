from application import include

urlpatterns = [
    include("/home", "home.urls")  # 引入了jsonrpc以后，务必每个蓝图的前缀必须补上。include函数中增加判断条件
]
