#Project : Create a Spotify Playlist using the Musical Time Machine
"""
PRACTISE: Web scraping over BeautifulSoup, Selenium
PROJECT: The user will type the date which she/he wants to search for. 
Via BeautifulSoup, scraping the top 100 song titles on that date into a Python List.
Authentication on Spotify via one of the most popular Python Spotify modules - Spotipy.
Create a new private playlist with the name "YYYY-MM-DD Billboard 100", where the date is the date you inputted
"""

import requests
from bs4 import BeautifulSoup
from datetime import date
import spotipy
from spotipy.oauth2 import SpotifyOAuth

HIT_SONG_URL = "https://www.billboard.com/charts/hot-100/"


user_day = int(input("Please enter the day(1-31): "))
user_month = int(input("Please enter the month(1-12): "))
user_year = int(input("Please enter the year(YYYY): "))

which_day = date(user_year, user_month, user_day)

response = requests.get(HIT_SONG_URL+f"{which_day}")
response_text = response.text
soup = BeautifulSoup(response_text, "html.parser")

top_10_list = soup.find_all(id="title-of-a-story")
top_list = soup.find_all(class_="o-chart-results-list__item")


singers = []
songs = []
top_1_song = soup.select_one(selector="#post-1479786 > div.charts-top-featured-alt.\/\/.lrv-a-wrapper.lrv-u-padding-lr-00\@mobile-max.u-padding-b-350\@tablet.u-padding-b-250.u-max-width-792.lrv-u-margin-lr-auto.lrv-a-grid.a-cols2\@tablet.u-grid-gap-250\@tablet.u-grid-gap-0 > div:nth-child(2) > div.lrv-u-flex.lrv-u-justify-content-space-between.lrv-u-margin-b-075.lrv-u-margin-b-00\@mobile-max.u-background-color-black\@mobile-max.u-color-white\@mobile-max.lrv-u-padding-lr-125\@mobile-max > div:nth-child(1) > div > div:nth-child(2) > h3 > a")
top_1_singer = soup.select_one(selector="#post-1479786 > div.charts-top-featured-alt.\/\/.lrv-a-wrapper.lrv-u-padding-lr-00\@mobile-max.u-padding-b-350\@tablet.u-padding-b-250.u-max-width-792.lrv-u-margin-lr-auto.lrv-a-grid.a-cols2\@tablet.u-grid-gap-250\@tablet.u-grid-gap-0 > div:nth-child(2) > div.lrv-u-flex.lrv-u-justify-content-space-between.lrv-u-margin-b-075.lrv-u-margin-b-00\@mobile-max.u-background-color-black\@mobile-max.u-color-white\@mobile-max.lrv-u-padding-lr-125\@mobile-max > div:nth-child(1) > div > div:nth-child(2) > p")
singers.append(top_1_singer.text.strip())
songs.append(top_1_song.text.strip())

singer_names = soup.find_all(class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")
song_lists = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

for name in singer_names:
    singers.append(name.text.strip())

for song in song_lists:
    songs.append(song.text.strip())


print(songs)
print(len(songs))


#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:4304/auth/spotify/callback",
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = user_year
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{which_day} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)