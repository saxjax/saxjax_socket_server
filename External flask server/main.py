import json
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
@app.route("/<data>")
def main(data=None):
    return data or json.dumps("the endpoint was called without data!")


@app.route('/int', methods=['GET', 'POST'])
def intelligent():
    msg = request.args.get('msg')
    count = request.args.get('count')
    print("intelligent called with")
    return f'test {msg} nr:{count}'


if __name__ == "__main__":
    app.run(debug=True, port=5001, host='0.0.0.0')
