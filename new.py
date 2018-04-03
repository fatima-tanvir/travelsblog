from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask("MyApp")

app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO( app )

@app.route("/gallery.html")
def gallery():
    return render_template("gallery.html")

@app.route('/contact.html')
def index():
	return render_template('contact.html')

@app.route('/process', methods=['POST'])
def process():

	email = request.form['email']
	name = request.form['name']


	if name and email:
		newName = 'Submited'

		return jsonify({'name' : newName})

	return jsonify({'error' : 'Missing data!'})

@app.route("/home.html")
def home():
    return render_template("home.html")

@app.route( '/chat.html' )
def Chat():
  return render_template( '/chat.html' )

def messageRecived():
    print( 'message was received!!!' )

@socketio.on( 'my event' )
def handle_my_custom_event( json ):
    print( 'recived my event: ' + str( json ) )
    socketio.emit( 'my response', json, callback=messageRecived )

if __name__ == '__main__':
  socketio.run( app, debug = True )
