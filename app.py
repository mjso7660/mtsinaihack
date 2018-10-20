from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('chat.html')

@app.route('/demo1')
def sessions1():
    return render_template('chat1.html')

@app.route('/demo2')
def sessions2():
    return render_template('chat2.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
#    //socketio.emit('my response', json, callback=messageReceived)
    socketio.emit('your response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)
