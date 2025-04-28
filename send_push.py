import requests
import json
from google.auth.transport.requests import Request
from google.oauth2 import service_account

# Path to your service account JSON file
SERVICE_ACCOUNT_FILE = '/Users/user/Downloads/firebase-key.json'

# Set up Firebase credentials using the service account file
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=["https://www.googleapis.com/auth/firebase.messaging"]
)

# Refresh the token if necessary
credentials.refresh(Request())

# Get the access token
ACCESS_TOKEN = credentials.token

# Define headers for the FCM request
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# Define the payload for the FCM push notification
payload = {
    "message": {
        "token": "fzkLAxPTNkqDmzTNoyZ44p:APA91bERMcbrrKtbTB_YrCU7mUr8rzSPPSJBY3BS9qXuURj3je63M4eYQtFvn5D4JXjgaSxmG8U53sWK5C_IXZdVKcfXuvYyEnHjrYGg-UfIMI5NbuozVYs",  # Replace with the FCM token of the device
        "notification": {
            "title": "Hello from GitHub Actions",
            "body": "This is a scheduled push"
        },
        "android": {
            "priority": "high"
        },
        "apns": {
            "headers": {
                "apns-priority": "10"
            }
        }
    }
}

# Convert the payload to JSON
json_data = json.dumps(payload)

# Send the request to FCM
response = requests.post(
    "https://fcm.googleapis.com/v1/projects/lite-360/messages:send",  # Replace with your project ID
    headers=headers,
    data=json_data
)

# Print the response status code and response text for debugging
print(response.status_code, response.text)
