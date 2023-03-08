from flask import Flask
# from debug import *


print("Start debug :)")


app = Flask(__name__)
app.config.from_pyfile('settings.py')


@app.route("/")
def index():
        print('test debug')
        return 'hi :)'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)


