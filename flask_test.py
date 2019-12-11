from flask import Flask, request, make_response
import json

app = Flask(__name__)


@app.route('/login/<username>&<password>')
def login(username, password):
    if username == '123' and password == '123':
        return json.loads(json.dumps({'code': 1}))
    else:
        return json.loads(json.dumps({'code': 0}))


@app.route('/')
def index():
    return json.loads(json.dumps({'hello': 'world'}))

@app.route('/indexx')
def indexx():
    return '2132112'


@app.route('/loging', methods=['GET', 'POST'])
def loging():
    if request.method == 'POST' or request.method == 'GET':
        date = request.get_data()
        print(date)
        res = make_response()
        res.set_cookie('name', '1235644')
        # raise Exception('121233213123error')
    return res


if __name__ == '__main__':
    app.run()
