from application import Flask, init_app

app: Flask = init_app("application.settings.dev")


@app.route('/')
def index():
    app.logger.debug("hello, debug")
    app.logger.info("hello, info")
    app.logger.warning("hello, warning")
    app.logger.error("hello, error")
    app.logger.critical("hello, critical")
    return 'welcome to yingmingApp'


if __name__ == '__main__':
    app.run()
