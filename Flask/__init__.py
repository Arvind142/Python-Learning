from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        somejson = request.get_json()
        return jsonify({"You sent : ": somejson}), 201
    else:
        return jsonify({"try": "sending some json"})


@app.route('/hello-world')
def hello_world():
    return jsonify({"About": "Hello World"})


@app.route('/multiply/<int:number>', methods=['GET'])
def get_multi(number):
    return jsonify({"square of " + str(number): number * number})


if __name__ == '__main__':
    app.run('localhost', 8081, debug=True)
