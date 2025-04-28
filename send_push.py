import os
import json
import requests
from google.oauth2 import service_account
import google.auth.transport.requests

# Path to your service account file
SERVICE_ACCOUNT_FILE = 'firebase-key.json'

# Get device token from environment
DEVICE_TOKEN = os.environ['FCM_DEVICE_TOKEN']

# Load credentials
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=["https://www.googleapis.com/auth/firebase.messaging"]
)

# Request access token
request = google.auth.transport.requests.Request()
credentials.refresh(request)
access_token = credentials.token

# FCM project ID (from your Firebase project settings)
PROJECT_ID = credentials.project_id

# FCM endpoint
url = f"https://fcm.googleapis.com/v1/projects/lite-360/messages:send"

# Construct the message payload
payload = {
    "message": {
        "token": DEVICE_TOKEN,
        "data": {
            "silent": "true"
        }
    }
}

# Set headers
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json; UTF-8",
}

# Send the request
response = requests.post(url, headers=headers, json=payload)

# Print response
print(response.status_code)
print(response.text)
