import requests
from urllib.parse import urlencode
import base64

import webbrowser

client_id = "YOUR_CLIENT_ID_HERE"
client_secret = "YOUR_CLIENT_SECRET_HERE"

auth_headers = {
	"client_id": client_id,
	"response_type": "code",
	"redirect_uri": "http://localhost:3000", # Change this to whatever URI you specified on the spotify developers portal
	"scope": "streaming,user-read-playback-state" 
}

webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))

#Once you receive the authorization code, comment the above line and paste the authorization code below

# paste the new Authorization code to get the authorization token
code = "YOUR_AUTHORIZATION_CODE_BELOW"



encoded_credentials = base64.b64encode(client_id.encode() + b':' + client_secret.encode()).decode("utf-8")
token_headers = {
	"Authorization": "Basic " + encoded_credentials,
	"Content-Type": "application/x-www-form-urlencoded"
}

token_data = {
	"grant_type": "authorization_code",
	"code": code,
	"redirect_uri": "http://localhost:3000" # Chnage this to whatever URI you specified on the spotify developers portal
}

r = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)

token = r.json()

print(token)