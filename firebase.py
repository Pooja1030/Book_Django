import os
import logging
import requests
import json

# Initialize logger
logger = logging.getLogger(__name__)

# Use an environment variable to define the path to the Firebase credentials
firebase_creds_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS', 'firebase/firebase-adminsdk.json')

# Check if Firebase credentials file exists
if not os.path.exists(firebase_creds_path):
    logger.error(f"Firebase credential file not found at '{firebase_creds_path}'")
else:
    # Initialize Firebase Admin SDK (only Firestore)
    from firebase_admin import credentials, firestore
    import firebase_admin

    cred = credentials.Certificate(firebase_creds_path)
    firebase_admin.initialize_app(cred)
    db = firestore.client()

# Firebase Auth URL
FIREBASE_AUTH_URL = "https://identitytoolkit.googleapis.com/v1/accounts:"

# Function to create a user with email and password
# Function to create a user with email and password
def create_user(email, password):
    api_key = "AIzaSyDl9peCQCMfpcXATbyv_quznL4g7QgzERo"  # Replace with your actual API key
    url = f"{FIREBASE_AUTH_URL}signUp?key={api_key}"  # Use the API key here
    data = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }

    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        logger.info("User created successfully.")
        return response.json()  # Contains user info and tokens
    else:
        logger.error("Error creating user: %s", response.text)
        return None


# Function to sign in a user with email and password
def sign_in_user(email, password):
    api_key = "AIzaSyDl9peCQCMfpcXATbyv_quznL4g7QgzERo"  # Replace with your actual API key
    url = f"{FIREBASE_AUTH_URL}signInWithPassword?key={api_key}"  # Correctly formatted URL
    data = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }

    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        logger.info("User signed in successfully.")
        return response.json()  # Contains user info and tokens
    else:
        logger.error("Error signing in user: %s", response.text)
        return None

# Example usage
if __name__ == "__main__":
    email = "user@example.com"  # Replace with actual email
    password = "your-password"   # Replace with actual password

    # Create user
    create_user_response = create_user(email, password)
    if create_user_response:
        print("User Created:", create_user_response)

    # Sign in user
    sign_in_response = sign_in_user(email, password)
    if sign_in_response:
        print("User Signed In:", sign_in_response)
