import requests
import collections

MovieResult = collections.namedtuple('MovieResult',
"imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres")

search = input("What would you like to search for?")
url = f'http://movie_service.talkpython.fm/api/search/{search}'

resp = requests.get(url)
resp.raise_for_status()

movie_data = resp.json()
movies_list = movie_data.get('hits')

movies = [
    MovieResult(**md)
    for md in movies_list
]

print(f"Found {len(movies)} movies for search: {search}.")
for m in movies:
    print(f"{m.year} -- {m.title}")

