from flask import Flask

app = Flask(__name__)


@app.route("/engine/approve", methods=['POST'])
def get_loan_approval():
    return "approval"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3005)
