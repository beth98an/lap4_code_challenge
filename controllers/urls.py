import sqlite3
import random
import string

def getUrls(data):
    return {'id': data[0], 'url': data[1],'short_url': data[2]}

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get(code):
    conn = get_db_connection()
    findUrl = conn.execute('SELECT * FROM shorten_url WHERE short_url = ?', (code,)).fetchall()
    if findUrl:
        getUrl = list(map(getUrls, findUrl))
        print(getUrl)
        conn.close()
        return getUrl[0]['url']
    else:
        return ''

def random_string():
    characters = string.ascii_lowercase + string.digits
    str = ''.join(random.choice(characters) for i in range(6))
    return str


def create(data):
    conn = get_db_connection()
    check = conn.execute('SELECT * FROM shorten_url WHERE url = ?', (data['urlsearch'],)).fetchall()
    if check :
        getUrl = list(map(getUrls, check))
        return getUrl[0]['short_url']
    else:
        getShort = random_string()
        addUrl = conn.execute('INSERT INTO shorten_url (url, short_url) VALUES (?, ?) RETURNING *', (data['urlsearch'], getShort))
        shortUrl = list(map(getUrls, addUrl))
        print(shortUrl)
        conn.commit()
        conn.close()
        return shortUrl[0]['short_url']
