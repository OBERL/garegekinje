import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase (only once)
if not firebase_admin._apps:
    cred = credentials.Certificate('C:/Users/BITLOCKER/Downloads/sasrws-bd7d0-firebase-adminsdk-dqadm-3a5c788049.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://sasrws-bd7d0-default-rtdb.firebaseio.com/'
    })
