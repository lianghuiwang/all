from flask import Flask

app = Flask(__name__)
#app.config.update(DEBUG=True)

#@app.route('/')就是将url中的/映射到hello_world这个视图函数上面


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
