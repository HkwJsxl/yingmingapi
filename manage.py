from application import Flask, init_app

app: Flask = init_app("application.settings.dev")


@app.route('/')
def index():
    return 'welcome to yingmingApp'


if __name__ == '__main__':
    app.run()
