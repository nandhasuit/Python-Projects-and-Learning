import sqlite3
import json

conn = sqlite3.connect('rostertrack.sqlite')
cur= conn.cursor()

cur.executescript('''DROP TABLE IF EXISTS user;
               DROP TABLE IF EXISTS member;
               DROP TABLE IF EXISTS course;

CREATE TABLE user(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT UNIQUE
            );
             
CREATE TABLE course(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            title TEXT UNIQUE
            );
            
CREATE TABLE member(
            user_id INTEGER,
            course_id INTEGER,
            role INTEGER,
            PRIMARY KEY(user_id, course_id)
            );
            ''')

fname = input('Enter the file name: ')
if len(fname) < 1:
    fname = 'roster_data_sample.json'
data = open(fname).read()
jdata = json.loads(data)

for i in jdata:
    name = i[0];
    title = i[1];

    print(name, title)

    cur.execute(''' INSERT OR IGNORE INTO user (name) VALUES (?)''',(name, ))
    cur.execute(''' SELECT id FROM user where name = ?''', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO course(title) VALUES(?)''', (title, ))
    cur.execute('''SELECT id FROM course WHERE title = ?''', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO member(user_id,course_id) VALUES (?,?)''', (user_id,course_id))

conn.commit()


