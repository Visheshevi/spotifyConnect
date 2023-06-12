import requests


# Grab the access Token you received from running the spotify_api_connect.py and paste it below
# Your Spotify access token
access_token = "YOUR_AUTHORIZATION_TOKEN_HERE"

# Prepare the headers for the request
headers = {
    "Authorization": f"Bearer {access_token}"
}

# Make the request
response = requests.get("https://api.spotify.com/v1/me/player/devices", headers=headers)

# Parse the JSON response
json_response = response.json()

if response.status_code == 200:
    # The request was successful
    devices = json_response["devices"]
    for device in devices:
        print(f"Device ID: {device['id']}, Device Name: {device['name']}")
else:
    # The request failed
    print(f"Failed to get devices: {json_response}")
