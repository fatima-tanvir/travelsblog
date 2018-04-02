from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask("MyApp")

app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO( app )

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/home")
def home():
    return render_template("new.html")

@app.route( '/Chat' )
def Chat():
  return render_template( './TravelChat.html' )

def messageRecived():
    print( 'message was received!!!' )

@socketio.on( 'my event' )
def handle_my_custom_event( json ):
    print( 'recived my event: ' + str( json ) )
    socketio.emit( 'my response', json, callback=messageRecived )

if __name__ == '__main__':
  socketio.run( app, debug = True )
