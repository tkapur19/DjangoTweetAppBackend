from django.http import HttpResponse
import simplejson as json
import tweepy
import pyrebase

# Function for handling request to obtain Latest tweets and passing them into Firebase Database
def get_tweets(request, username):


    ckey = "4aCpfAqJGtsyJAT8hXz7pYy9P"
    csecret = "Ejc0XYVMgUVEas9TXYxZExILHFsnVwyatfRyT4o2eC9KvE0XFQ"
    atoken = "440893181-ooOe3hDIHNcmqF3T9DInbmJKPw8M3hiimGhP9WW7"
    asecret = "hsMifowUxWVWSbzPpqbJ3UJRV9DYXyy7SU1azklBS0POw"
    auth = tweepy.OAuthHandler(ckey, csecret)

    auth.set_access_token(atoken, asecret)

    api = tweepy.API(auth)

    # Getting latest timeline of twitter User obtaining its userName from Get request by the client

    stuff = api.user_timeline(screen_name=str(username), count=1, include_rts=False)

    # Fetching Json response from the status object obtained

    stuff1=stuff[0]

    json_str = json.dumps(stuff1._json)

    # Creating Firebase Connection
    # Making dictionary of required keys
    config = {
        "apiKey": "AIzaSyCMc-5ukwMNvcNgzvrH0JFGLbrWLEaIqOg",
        "authDomain": "gettingtweets.firebaseapp.com",
        "databaseURL": "https://gettingtweets.firebaseio.com",
        "storageBucket": "gettingtweets.appspot.com",
    }
    # initialising firebase
    firebase = pyrebase.initialize_app(config)

    # Firebase Authentication
    auth = firebase.auth()
    # authenticate a user
    user = auth.sign_in_with_email_and_password("1tarun.kapur@gmail.com", "mySuperStrongPassword")

    # Getting Firebase Database Instance( as db)
    db = firebase.database()
    # Passing the Json response in Firebase

    db.child(str(username)).set(json_str, user['idToken'])


    return HttpResponse(json_str)