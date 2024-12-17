from flask import Flask
import sqlite3
conn = sqlite3.connect('podarki.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE podarki (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fio TEXT NOT NULL,
    podarok TEXT NOT NULL,
    price INTEGER,
    status TEXT NOT NULL
)
''')

cursor.execute("INSERT  INTO podarki (fio, podarok, price, status) VALUES ('И. Иван', 'traxxs slash  4/4', 55000, 'не куплен')")
cursor.execute("INSERT  INTO podarki (fio, podarok, price, status) VALUES ('К. Мария', 'медведь', 6000, 'куплен')")
cursor.execute("INSERT  INTO podarki (fio, podarok, price, status) VALUES ('Ш. Николай', 'ружье', 30000, 'не куплен')")
cursor.execute("INSERT  INTO podarki (fio, podarok, price, status) VALUES ('П. Иван', 'футбольный мяч', 4000, 'не куплен')")
cursor.execute("INSERT  INTO podarki (fio, podarok, price, status) VALUES ('Б. Сергей', 'бита', 70000, 'куплен')")
cursor.execute("INSERT  INTO podarki (fio, podarok, price, status) VALUES ('П. Азат', 'рогатка', 2000, 'не куплен')")
cursor.execute("INSERT  INTO podarki (fio, podarok, price, status) VALUES ('Л. Амир', 'настольная игра', 2000, 'не куплен')")
cursor.execute("INSERT  INTO podarki (fio, podarok, price, status) VALUES ('Б. Екатерина', 'сертификат в салон красоты', 30000, 'куплен')")
cursor.execute("INSERT  INTO podarki (fio, podarok, price, status) VALUES ('И. Ирик', 'игровое кресло', 20000, 'не куплен')")
cursor.execute("INSERT  INTO podarki (fio, podarok, price, status) VALUES ('В.Владимир', 'traxxas trx4', 60000, 'не куплен')")
conn.commit()

conn.close()

