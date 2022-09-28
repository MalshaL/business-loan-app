from flask import Flask, make_response, jsonify
from flask import request
import requests
import random

app = Flask(__name__)


@app.route("/accounts/balanceSheet", methods=['POST', 'OPTIONS'])
def get_balance_sheet():
    if request.method == 'OPTIONS':
        return _build_preflight_response()
    elif request.method == 'POST':
        print(request.json)
        # generate user id
        uid = random.randint(10000, 99999)
        # obtain account provider for the user
        acc_provider = request.json['accProvider']
        # set user id as parameter to be passed to third party
        params = {"user_id": uid}

        # call third party api to get balance sheet
        response = ''
        if acc_provider == 'xero':
            response = requests.post(url='http://localhost:3006/financialStatements/balanceSheet', data=params).json()
        elif acc_provider == 'myob':
            response = requests.post(url='http://localhost:3007/report/balanceSheetSummary', data=params).json()
        print(response)
        return _build_response(jsonify(response))
    else:
        raise RuntimeError("Unsupported method {}".format(request.method))


def _build_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response


def _build_response(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
