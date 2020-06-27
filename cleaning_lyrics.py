import json
import re

with open('Lyrics_JoaquínSabina.json') as json_file:
    data = json.load(json_file)

lyrics_list = []

for x in range(100):
    lyric = data["songs"][x]["lyrics"]
    lyric_clean = re.sub(r'\[(.*?)\]', '', lyric)
    lyrics_list.append(lyric_clean)

separator = '\n \n<|endoftext|>\n \n'

lyrics = separator.join(lyrics_list)

f = open( 'lyrics_JS.txt', 'w')
f.write(lyrics)
f.close()

