from flask import Flask, jsonify, request, make_response
import random


app = Flask(__name__)


@app.route("/user/getUser", methods=['POST', 'OPTIONS'])
def get_user():
    if request.method == 'OPTIONS':
        return _build_preflight_response()
    elif request.method == 'POST':
        uid = random.randint(10000, 99999)
        return _build_response(jsonify({'uid': uid}))


# fix cors - response for POST call
def _build_response(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# fix cors - response for OPTIONS call
def _build_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
