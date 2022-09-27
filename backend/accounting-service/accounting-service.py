from flask import Flask

app = Flask(__name__)


@app.route("/accounts/balanceSheet")
def save_new_application():
    # connect to third party
    return "balance sheet"
