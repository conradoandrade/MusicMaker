import requests
import os
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import gpt 
import re

spotify_dir = "Spotfy"
covers_dir = os.path.join(spotify_dir, 'covers')
tracks_dir = os.path.join(spotify_dir, 'tracks')
data_dir = "DATA"
known_songs_file = "KNOWNsongs.json"

os.makedirs(spotify_dir, exist_ok=True)
os.makedirs(covers_dir, exist_ok=True)
os.makedirs(tracks_dir, exist_ok=True)
os.makedirs(data_dir, exist_ok=True)

answer_name = gpt.main()  
name = re.sub(r'[^a-zA-Z0-9_]', '', answer_name.replace(' ', ' - '))
print(f"modified_ answer_name: {name}")

known_songs_path = os.path.join(data_dir, known_songs_file)

known_data = []

def get_song():

    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    results = spotify.search(q=name, type='track')
    print(f"spotfy read :{answer_name}")

    song_path = None 

    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        preview_url = track.get('preview_url')

        if preview_url and not any(song['song'] == track.get('name', 'Unknown track') for song in known_data):
            response = requests.get(preview_url)
            song_path = os.path.join(tracks_dir, f"{name}.mp3") 
            with open(song_path, 'wb') as outfile:
                outfile.write(response.content)


            with open(known_songs_path, 'w') as outfile:
                json.dump(known_data, outfile, indent=4)
        print()

    return name, song_path  # Return song name and path
