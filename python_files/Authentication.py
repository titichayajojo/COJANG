import pyrebase
from getpass import getpass

firebaseConfig = {
    "apiKey": "AIzaSyA5Baw-V75EI5JLy1eTkNL1LHZq4-U3hUE",
    "authDomain": "cojang-1a1ac.firebaseapp.com",
    "databaseURL": "",
    "projectId": "cojang-1a1ac",
    "storageBucket": "cojang-1a1ac.appspot.com",
    "messagingSenderId": "561371940594",
    "appId": "1:561371940594:web:15f3d56106a371cc43f26b",
    "measurementId": "G-62KXCNH3S0"
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

email = input("Please Enter Your Email Address : \n ")
password = getpass("Please Enter Your Password : \n ")

user = auth.create_user_with_email_and_password(email,password)

#for reset password
#auth.send_password_reset_email(email)

print("Success...")