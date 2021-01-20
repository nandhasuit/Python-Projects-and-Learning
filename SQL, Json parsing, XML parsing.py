import xml.etree.ElementTree as ET
import sqlite3
import ssl


conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()
cur.executescript('''DROP TABLE IF EXISTS artist;
                     DROP TABLE IF EXISTS album;
                     DROP TABLE IF EXISTS genre;
                     DROP TABLE IF EXISTS track;
CREATE TABLE artist(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT UNIQUE);
CREATE TABLE album(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                album_name TEXT UNIQUE,
                artist_id INTEGER );
CREATE TABLE genre(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                genre_name TEXT UNIQUE);
CREATE TABLE track(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                title TEXT UNIQUE,
                rating INTEGER len INTEGER count INTEGER,
                album_id INTEGER);''')

def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None


fname = 'Library.xml'
fh = ET.parse(fname)
all = fh.findall('dict/dict/dict')
for e in all:
    print(lookup(e,'Name'))
    name =lookup(e,'Name')
    cur.execute('INSERT OR IGNORE INTO artist (name) VALUES(?)', (name, ))
    conn.commit()