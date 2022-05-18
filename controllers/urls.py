import sqlite3

def getUrls(data):
    return {'id': data[0], 'url': data[1],'short_url': data[2]}

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get(code):
    conn = get_db_connection()
    findUrl = conn.execute('SELECT * FROM shorten_url WHERE short_url = ?', (code,)).fetchall()
    getUrl = list(map(getUrls, findUrl))
    return getUrl[0]['url']
