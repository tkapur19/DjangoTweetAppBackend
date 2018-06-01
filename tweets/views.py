from django.http import HttpResponse
import simplejson as json
import tweepy
import pyrebase
import twitter
def get_tweets(request,username):
    ckey = "4aCpfAqJGtsyJAT8hXz7pYy9P"

    csecret = "Ejc0XYVMgUVEas9TXYxZExILHFsnVwyatfRyT4o2eC9KvE0XFQ"

    atoken = "440893181-ooOe3hDIHNcmqF3T9DInbmJKPw8M3hiimGhP9WW7"

    asecret = "hsMifowUxWVWSbzPpqbJ3UJRV9DYXyy7SU1azklBS0POw"

    auth = tweepy.OAuthHandler(ckey, csecret)

    auth.set_access_token(atoken, asecret)

    api = tweepy.API(auth)

    stuff = api.user_timeline(screen_name=str(username), count=1, include_rts=False)
    
    stuff1=stuff[0]

    json_str = json.dumps(stuff1._json)


    config = {
        "apiKey": "AIzaSyCMc-5ukwMNvcNgzvrH0JFGLbrWLEaIqOg",
        "authDomain": "gettingtweets.firebaseapp.com",
        "databaseURL": "https://gettingtweets.firebaseio.com",
        "storageBucket": "gettingtweets.appspot.com",
    }
    firebase = pyrebase.initialize_app(config)

    auth = firebase.auth()
    # authenticate a user
    user = auth.sign_in_with_email_and_password("1tarun.kapur@gmail.com", "mySuperStrongPassword")

    db = firebase.database()
    db.child(str(username)).set(json_str, user['idToken'])




    return HttpResponse(json_str)