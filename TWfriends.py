import urllib.request, urllib.parse, urllib.error
import ssl
import json
import sqlite3
import twurl

conn = sqlite3.connect('friendsdb.sqlite')
cur = conn.cursor()

tw_url = 'https://api.twitter.com/1.1/friends/list.json'

cur.execute('''CREATE TABLE IF NOT EXISTS Email (id INTEGER PRIMARY KEY AUTOINCREMENT , account TEXT, email_id TEXT)''')



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

acc = input('Enter the account name: ')
urls = twurl.augment(tw_url, {'screen_name': acc, 'count': '100'})
conne = urllib.request.urlopen(urls, context= ctx)
data = conne.read().decode()
fd = json.loads(data)

for i in fd['users']:
    friend = i['screen_name']
    url = i['url']
    print(friend,url)
    cur.execute('''INSERT OR IGNORE INTO Email
                            (account, email_id) VALUES (?, ?)''', (friend, url))
    conn.commit()






