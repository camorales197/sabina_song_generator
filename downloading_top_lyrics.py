## Script to download all the lirycs from a singer

import lyricsgenius
from dotenv import load_dotenv
import os


load_dotenv()

GENIUS_API = os.environ.get("GENIUS_APIKEY")
print(GENIUS_API)

genius = lyricsgenius.Genius(GENIUS_API)
artist = genius.search_artist("Joaquín Sabina", max_songs=500, sort="title")

#song = genius.search_song("To You", "Joaquín Sabina")
artist.save_lyrics()
