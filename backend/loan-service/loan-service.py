from flask import Flask

app = Flask(__name__)


@app.route("/loan/newApplication")
def save_new_application():
    return "appid"


@app.route("/loan/approval")
def get_approval():
    # connect to decision engine
    return "approval"
