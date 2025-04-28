from google.oauth2 import service_account
from google.auth.transport.requests import Request
import requests
import json

# Path to the Firebase service account key
SERVICE_ACCOUNT_FILE = 'firebase-key.json'

# Load the credentials
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=["https://www.googleapis.com/auth/firebase.messaging"]
)

# Refresh the token if needed
credentials.refresh(Request())

ACCESS_TOKEN = credentials.token

# Define headers for the HTTP request
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# FCM message payload
message = {
    "message": {
        "token": "<FCM_DEVICE_TOKEN>",
        "notification": {
            "title": "Test Notification",
            "body": "This is a test push notification"
        }
    }
}

# Send the message via FCM
response = requests.post(
    'https://fcm.googleapis.com/v1/projects/<YOUR_PROJECT_ID>/messages:send',
    headers=headers,
    data=json.dumps(message)
)

print(response.status_code)
print(response.text)
