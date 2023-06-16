import logging
from logging.handlers import RotatingFileHandler  # 按文件大小分割日志文件
from logging.handlers import TimedRotatingFileHandler  # 按时间片分割日志文件
from flask import Flask


class Logger(object):
    """日志配置类"""

    def __init__(self, app: Flask = None):
        """
        日志实例化
        :param app: 当前flask应用实例对象
        """
        if app:
            self.init_app(app)

    def init_app(self, app: Flask = None) -> None:
        """
        读取项目的日志配置项
        :param app: 当前flask应用实例对象
        :return: None
        """
        self.app = app
        self.log_file = self.app.BASE_DIR / self.app.config.get("LOG_FILE", 'logs/app.log')
        self.log_level = self.app.config.get("LOG_LEVEL", 'INFO')
        self.log_backpu_count = self.app.config.get("LOG_BACKPU_COUNT", 31)
        self.log_format = self.app.config.get("LOG_FORMAT",
                                              '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
        self.log_rotating_time = self.app.config.get("LOG_ROTATING_TIME", "midnight")
        self.log_charseter = self.app.config.get("LOG_charseter", 'UTF-8')
        self.log_file_size = self.app.config.get("LOG_FILE_SIZE", 300 * 1024 * 1024)
        self.setup()

    def setup(self) -> None:
        """
        把日志功能安装到flask项目中
        :return:
        """
        # from logging.handlers import TimedRotatingFileHandler 按时间片分割日志
        handler: TimedRotatingFileHandler = TimedRotatingFileHandler(
            filename=self.log_file,  # 日志存储的文件路径
            when=self.log_rotating_time,  # 每天备份日志的时间，午夜
            backupCount=self.log_backpu_count,  # 备份数量
            encoding=self.log_charseter  # 日志文件编码
        )

        # from logging.handlers import RotatingFileHandler      按文件大小分割日志
        # handler: RotatingFileHandler = RotatingFileHandler(
        #     filename=self.log_file,
        #     maxBytes=self.log_file_size,
        #     backupCount=self.log_backpu_count,
        #     encoding=self.log_charseter # 日志文件编码
        # )

        # 设置日志信息的等级
        handler.setLevel(self.log_level)

        # 日志信息的格式
        logging_format: logging.Formatter = logging.Formatter(self.log_format)
        handler.setFormatter(logging_format)

        self.app.logger.addHandler(handler)
