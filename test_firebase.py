import pyrebase

#config firebase
config = {
    "apiKey": "AIzaSyCTm1zh_IyOetzQ2uZvi1ZV5X4fXZxIdT8",
    "authDomain": "uh-hackathon.firebaseapp.com",
    "databaseURL": "https://uh-hackathon-default-rtdb.firebaseio.com",
    "storageBucket": "uh-hackathon.appspot.com"
    }

firebase = pyrebase.initialize_app(config)

database = firebase.database()
database.update({"time_save": "Hello"})
         
         