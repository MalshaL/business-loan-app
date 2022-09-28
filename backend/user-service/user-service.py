from flask import Flask, jsonify
import random


app = Flask(__name__)


@app.route("/user/getUser", methods=['POST'])
def get_user():
    uid = random.randint(10000, 99999)
    return jsonify({'uid': uid})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
