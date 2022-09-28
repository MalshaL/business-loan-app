from flask import Flask

app = Flask(__name__)


@app.route("/loan/newApplication")
def save_new_application():
    return "appid"


@app.route("/loan/getApproval")
def get_approval():
    # connect to decision engine
    return "approval"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
