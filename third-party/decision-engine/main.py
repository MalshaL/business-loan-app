from flask import Flask, jsonify, request, make_response

app = Flask(__name__)


@app.route("/engine/approve", methods=['POST', 'OPTIONS'])
def get_loan_approval():
    if request.method == 'OPTIONS':
        return _build_preflight_response()
    elif request.method == 'POST':
        data = request.get_json()
        print(data)
        # assumption: reject application if profit in the last 12 months is zero or a loss
        # or if loan amount is 5x larger than avg assets in last 12 months
        data['approval'] = False if data['profit_pa'] < 0 or data['avg_assets_pa'] * 5 < data['loan_amount'] else True
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
    app.run(host='0.0.0.0', port=3005)
