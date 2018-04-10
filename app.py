from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import tweepy

app = Flask("MyApp")

app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO( app )

@app.route("/gallery.html")
def gallery():
    auth = tweepy.OAuthHandler("0SKohKeusYV36sM7bKgLil0LZ","6aoAyxWbEhGjCrpv1EWSBEtXK5I10lsdiJAJlXm9lvf7E1v4XL")
    auth.set_access_token ("701267940885340161-mt2uIgz9vMPSFAzRtAkQjeZIqOp54er", "dkznlFrYZkIZyf0HI0X60xEXMaicnR2O1XwoWksJoLejO")

    twitter_api = tweepy.API(auth)

    travel_tweets = twitter_api.search(
    	#Twitter handles what you want to search by
    	q = "Travel",
    	r = "World",
    	s = "Traveling",
    	t = "traveler",
    	u = "worldwonder",
    	v = "wanderlust",
    	w = "ilovetravel",
    	y = "trip",
    	a = "holiday"
    )

    return render_template("gallery.html", travel_tweets=[tweet.user.name + ":" + tweet.text for tweet in travel_tweets])

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
