import json
from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret!"
sock = SocketIO(app)


#fun functionality
# @app.route('/reverse')
# def reverse(ws):
#     while True:
#         text = ws.receive()
#         ws.send(text)  # to reverse string: ws.send(text[::-1])

@app.route("/<data>")
def gotData(data=None):
    print(data or "no data")
    return data or json.dumps("the endpoint was called without data!")

#Standard http server functionality
#call ip:port/intelligent?msg=great_to_work_at_intelligent_systems&count=2
@app.route('/intelligent', methods=['GET', 'POST'])
def intelligent():
    msg = request.args.get('msg')
    count = request.args.get('count')
    print(f'intelligent called with {msg} and {count}')
    return f'test {msg} nr:{count}'


#socket functionality
#renders the html in main.html
#main.html listens for 'connect'(no functionality paired) and 'message'(prints the received message) ,
@app.route("/")
def main(data=None):
    return render_template("main.html")

#when something connects connected message is send to all connected
@sock.on('connect')
def connecting():
    sock.send('connected')

#when something disconnects disconnected message is send to all connected
@sock.on('disconnect')
def connecting():
    sock.send('disconnected')

#when something connected sends a message, the message is send to all connected
@sock.on('message')
def handlemsg(msg):
    sock.send(msg)


#all hosts can access the server on their localhost og computername.local:5001
if __name__ == "__main__":
    sock.run(app, debug=True, port=5001, host='0.0.0.0')
