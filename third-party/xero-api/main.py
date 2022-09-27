from flask import Flask
import json

app = Flask(__name__)


@app.route("/financialStatements/balanceSheet", methods=['POST'])
def get_balance_sheet():
    data_file = open('mock-data.json')
    data = json.load(data_file)
    data_file.close()
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3006)
