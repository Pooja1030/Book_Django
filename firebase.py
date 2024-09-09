import os
import logging
from firebase_admin import credentials, firestore
import firebase_admin

logger = logging.getLogger(__name__)

# Check if Firebase credentials file exists
if not os.path.exists('firebase/firebase-adminsdk.json'):
    logger.error("Firebase credential file not found at 'firebase/firebase-adminsdk.json'")
else:
    # Initialize Firebase
    cred = credentials.Certificate('firebase/firebase-adminsdk.json')
    firebase_admin.initialize_app(cred)

    # Initialize Firestore
    db = firestore.client()
