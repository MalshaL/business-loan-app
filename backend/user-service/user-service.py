from flask import Flask

app = Flask(__name__)


@app.route("/user/newUser")
def add_new_user():
    return "uid"

