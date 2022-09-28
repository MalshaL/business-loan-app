from flask import Flask

app = Flask(__name__)


@app.route("/user/getUser", methods=['POST'])
def get_user():
    return "uid"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
