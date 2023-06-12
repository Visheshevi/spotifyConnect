# spotifyConnect

Project to connect to the Spotify API. This repo is a sample project to run spotify on a specific device

# Getting Started

1. Create a spotify developers account. 
2. Go to the Dashboard on your developers homepage and create an App. Provide the app name, Redirect URI(a URL that if called on, can run your app)

Once you have created an app, clone this repo

There are three files to get your job done:
1. spotify_api_connect.py
2. spotify_get_device_ids.py
3. spotify_start_on_device.py


The *spotify_api_connect.py* is used to get an authorization code, that would be used to authorize against your spotify user profile. This project would be updated to avoid getting an authorization code every hour. 

The *spotify_get_device_ids.py* is used to get the list of all the devices your spotify is connected to. Grab the device ID you want to run spotify on and paste it in the *spotify_start_on_device.py*. Run this file an listen to the last song being played on your spotify 