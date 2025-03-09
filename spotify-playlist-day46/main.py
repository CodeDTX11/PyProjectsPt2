from pprint import pprint
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"

spotify_client_id = os.environ.get("SPOTIFY_CLIENT_ID")
spotify_secret = os.environ.get("SPOTIFY_SECRET")

date = "2001-09-10"
# date = input("Enter date: ")
year = date.split("-")[0]

full_url = BILLBOARD_URL + date
F = True
song_names = []

if F:
    response = requests.get(full_url, headers=header)
    web_html = response.text

    soup = BeautifulSoup(web_html, "html.parser")

    # song_tag = soup.find(name="h3", id="title-of-a-story", class_="c-title")
    song_names_spans = soup.select("li ul li h3")

    song_names = [song.getText().strip() for song in song_names_spans]
    # print(song_names)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=spotify_client_id,
        client_secret=spotify_secret,
        show_dialog=True,
        cache_path="token.txt",
        username="dm5messerly"
    )
)
user_id = sp.current_user()["id"]

song_uris = []

for name in song_names[:3]:
    item = sp.search(q=f"track:{name} year:{year}", type="track", limit=1)
    try:
        song_uris.append(item['tracks']['items'][0]['uri'])
    except KeyError:
        print(f"{name} not found")

# pprint(item['tracks']['items'][0]['uri'])
# print(song_uris)

new_playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False, description="idk man")

# print(playlist_id["id"])

sp.playlist_add_items(playlist_id=new_playlist["id"], items=song_uris)

