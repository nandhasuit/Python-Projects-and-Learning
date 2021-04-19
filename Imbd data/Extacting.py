import json
import sqlite3
import re
import urllib.parse, urllib.request,urllib.request
import ssl
from bs4 import BeautifulSoup
import requests

url = "http://www.imdb.com/chart/top"

conn = sqlite3.connect("movie data.sqlite")
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Movie 
            (movie_title TEXT,
            year INTEGER,
            place INTEGER,
            star_cast TEXT,
            rating INTEGER,
            vote INTEGER,
            link TEXT,
            movie_poster BLOB
            )''')



ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE




data = urllib.request.urlopen(url,context=ctx)
soup = BeautifulSoup(data, 'html.parser')

movies = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
votes = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=nv]')]

for j in range(0,len(movies)):
    ms = movies[j].get_text()
    m = (' '.join(ms.split()).replace('.',''))
    mt = m[len(str(j))+1: -7]
    year = re.search(r'\((.*?)\)', ms).group(1)
    place = m[:len(str(j)) - (len(m))]



    data = {"movie_title": mt,
            "year": year,
            "place": place,
            "star_cast": crew[j],
            "rating": ratings[j],
            "vote": votes[j],
            "link": links[j]}

    flink = "http://www.imdb.com" + data['link']

    imgdata = urllib.request.urlopen(flink, context=ctx)
    soup = BeautifulSoup(imgdata, 'html.parser')
    img = json.loads(soup.find('script', type='application/ld+json').text)
    movie_pic = img['image']

    cur.execute('''INSERT OR IGNORE INTO Movie (movie_title,year,place,star_cast,rating,vote,link,movie_poster) 
    VALUES ( ?, ?, ?, ?, ?, ?, ?,?)''', (data["movie_title"],data["year"],data["place"],data["star_cast"],data["rating"],data["vote"],data["link"],movie_pic))
    conn.commit()








