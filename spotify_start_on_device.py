import requests

# Paste the device ID you want to play spotify on from the list you got by running the spotify_get_device_ids.py
# Replace these with your actual Spotify OAuth token and device ID
spotify_token = "YOUR_AUTHORIZATION_TOKEN_HERE"
spotify_device_id = "YOUR_DEVICE_ID_HERE"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {spotify_token}",
}

response = requests.put(
    f"https://api.spotify.com/v1/me/player/play?device_id={spotify_device_id}", 
    headers=headers
)

if response.status_code == 204:
    print("Playback started successfully")
else:
    print(f"Failed to start playback: {response.content}")