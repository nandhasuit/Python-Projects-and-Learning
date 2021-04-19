import extacting
import urllib.parse, urllib.request,urllib.request
import ssl
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import requests

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.imdb.com/title/tt0053198/"
da = urllib.request.urlopen(url,context= ctx)
soup = BeautifulSoup(da, 'html.parser')
img = soup.select('script.typ')
for i in img:
    print(i)
