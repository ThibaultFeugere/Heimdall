#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

connection = sqlite3.connect("base.db")
cursor = connection.cursor()

pseudo = ('thibault',)

requete = cursor.execute('SELECT * FROM users WHERE username = ?', pseudo)
resultat = requete.fetchone()

print(resultat, resultat[1])

req = cursor.execute('SELECT * FROM users')
res = req.fetchall()

print(res)

reque = cursor.execute('SELECT * FROM users')

for row in reque.fetchall():
    print(row)

connection.close()