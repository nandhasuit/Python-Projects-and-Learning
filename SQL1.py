import string
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS COUNTS (Email TEXT,Count INTEGER)')

file = 'mbox.txt'
fh = open(file)
count = dict()
for line in fh:
    if not line.startswith("From "): continue
    words = line.split()
    email = words[1]
    cur.execute('SELECT Count FROM COUNTS WHERE Email = ?', (email, ))
    row = cur.fetchone()

    if row is None:
        cur.execute('INSERT INTO COUNTS (Email, Count) VALUES (?, 1)', (email, ))
    else:
        cur.execute('UPDATE COUNTS SET Count = Count + 1 WHERE Email = ?', (email, ))

cur.execute('SELECT Email, Count FROM COUNTS ORDER BY Count DESC')
conn.commit()





