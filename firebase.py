import os
import logging
from firebase_admin import credentials, firestore
import firebase_admin

logger = logging.getLogger(__name__)

# Use an environment variable to define the path to the Firebase credentials
firebase_creds_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS', 'firebase/firebase-adminsdk.json')

# Check if Firebase credentials file exists
if not os.path.exists(firebase_creds_path):
    logger.error(f"Firebase credential file not found at '{firebase_creds_path}'")
else:
    # Initialize Firebase
    cred = credentials.Certificate(firebase_creds_path)
    firebase_admin.initialize_app(cred)

    # Initialize Firestore
    db = firestore.client()
