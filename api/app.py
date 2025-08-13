from flask import Flask, request
from plotting import generateImg
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/plot', methods=["POST"])
def plot():
    data = request.get_json()

    return generateImg(data.get('funcs'), data.get('min'), data.get('max'))


if __name__ == "__main__":
    app.run()

