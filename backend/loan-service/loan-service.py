from flask import Flask, jsonify, make_response, request
import requests


app = Flask(__name__)


@app.route("/loan/newApplication")
def save_new_application():
    return "app id"


@app.route("/loan/getApproval", methods=['POST', 'OPTIONS'])
def get_approval():
    if request.method == 'OPTIONS':
        return _build_preflight_response()
    elif request.method == 'POST':
        balance_data = request.json['data']
        user_data = request.json['user']
        loan_amount = float(user_data['loanAmount'])

        # calculate profit and average assets in last 12 months
        profit, avg_assets = _get_balance_summary(balance_data)
        print(profit, '-', avg_assets)

        # get preassessment value
        preassessment_value = _get_preassessment_value(profit, avg_assets, loan_amount)

        # params to send to decision engine
        params = {
            'business_name': user_data['businessName'],
            'est_year': user_data['estYear'],
            'profit_pa': profit,
            'avg_assets_pa': avg_assets,
            'preassess_val': preassessment_value,
            'loan_amount': loan_amount
        }

        # connect to decision engine
        response = requests.post(url='http://localhost:3005/engine/approve', json=params).json()
        print(response)
        return _build_response(jsonify(response))


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


# get profit in last 12 months
def _get_balance_summary(balance_data):
    profit = 0
    assets = 0
    i = 0
    for entry in balance_data:
        if i > 12:
            break
        profit += entry['profitOrLoss']
        assets += entry['assetsValue']
        i += 1
    return profit, assets/i


def _get_preassessment_value(profit, avg_assets, loan_amount):
    # set default pre assessment value
    preassessment_value = 20

    if profit > 0:
        preassessment_value = 60
    elif avg_assets > loan_amount:
        preassessment_value = 100
    return preassessment_value


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
