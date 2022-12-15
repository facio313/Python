from flask import Flask, jsonify, render_template
from subprocess import call
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.secret_key = "mysecret"

socket_io = SocketIO(app)

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/')
@app.route('/allready')
def allready():
    return render_template('allready.html')

@socket_io.on("message")
def request(message):
    print("message : "+ message)
    mydict = dict()
    mydict['message'] = message
    send(mydict, broadcast=True)
    # broadcast : 다 보내는 거
    # echo : 보낸 사람에게 다시 돌려주는 거
    
@app.route('/canvas')
def canvas():
    return render_template('canvas.html')


if __name__ == '__main__':
    socket_io.run(app, host="192.168.35.51", debug=True, port=9999)
    

#pip install --upgrade python-socketio==4.6.0

#pip install --upgrade python-engineio==3.13.2

#pip install --upgrade Flask-SocketIO==4.3.1