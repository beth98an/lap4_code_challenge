import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute('INSERT INTO shorten_url (url, short_url) VALUES (?, ?)',('www.getfutureproof.co.uk', 'ufh8hd'))

cur.execute('INSERT INTO shorten_url (url, short_url) VALUES (?, ?)',('www.google.co.uk', 'sei6f8'))

connection.commit()
connection.close()
