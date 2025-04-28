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
    "Authorization": "Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# FCM message payload
message = {
    "message": {
        "token": "fzkLAxPTNkqDmzTNoyZ44p:APA91bERMcbrrKtbTB_YrCU7mUr8rzSPPSJBY3BS9qXuURj3je63M4eYQtFvn5D4JXjgaSxmG8U53sWK5C_IXZdVKcfXuvYyEnHjrYGg-UfIMI5NbuozVYs",
        "notification": {
            "title": "Test Notification",
            "body": "This is a test push notification"
        }
    }
}

# Send the message via FCM
response = requests.post(
    'https://fcm.googleapis.com/v1/projects/lite-360/messages:send',
    headers=headers,
    data=json.dumps(message)
)

print(response.status_code)
print(response.text)
