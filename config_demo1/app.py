from flask import Flask,request
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/list/')
def article_list():
    return 'article list'


@app.route('/p/<article_id>')
def article_detail(article_id):
    return '您请求的文章是: %s' % article_id


@app.route('/article/<string:test>')
def test_article(test):
    return 'test article'


@app.route('/u/<uuid:user_id>/')
def user_detail(user_id):
    return '用户个人中心页面: %s' % user_id


@app.route('/<any(blog,yser):url path>/<id>/')
def detail(url_path,id):
    if url_path == 'blog':
        return '博客详情： %s' % id
    else:
        return '用户详情: %s' % id


@app.run('/d/')
def d():
    wd = request.args.get('wd')
    return '您通过查询字符串的方式传递的参数是： %s' % wd


if __name__ == '__main__':
    app.run()
