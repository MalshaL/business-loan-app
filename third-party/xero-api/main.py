from flask import Flask, jsonify, request, make_response
import json

app = Flask(__name__)


@app.route("/financialStatements/balanceSheet", methods=['POST', 'OPTIONS'])
def get_balance_sheet():
    if request.method == 'OPTIONS':
        return _build_preflight_response()
    elif request.method == 'POST':
        data_file = open('mock-data.json')
        data = json.load(data_file)
        data_file.close()
        return _build_response(jsonify({'data': data}))


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
    app.run(host='0.0.0.0', port=3006)
