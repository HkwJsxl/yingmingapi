from flask import Flask


class Config(object):
    """项目配置加载类"""

    def __init__(self, app: Flask = None, config_path: str = None):
        if app:
            self.init_config(app, config_path)

    def init_config(self, app: Flask = None, path: str = None):
        """
        项目配置初始化函数
        :param app: 当前flask应用实例对象[python中的对象属于引用类型，所以函数内部改了app的数据，外界的app也会修改]
        :param path: 配置文件的导包路径   application.settings.dev
        :return:
        """
        # 先加载默认配置settings.__init__，然后加载当前指定配置config_path
        init_path: str = ".".join(path.split(".")[:-1])
        app.config.from_object(init_path)  # 先加载settings.__init__
        app.config.from_object(path)  # 再加载settings.dev或者settings.prod
