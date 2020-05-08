#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3

connection = sqlite3.connect("base.db")
cursor = connection.cursor()

pseudo = ('thibault',)

requete = cursor.execute('SELECT * FROM users WHERE username = ?', pseudo)
resultat = requete.fetchone()
username = resultat[1]

print(resultat, username)

new_user = (cursor.lastrowid, "Jason", "secret")
cursor.execute('INSERT INTO users VALUES (?, ?, ?)', new_user)
connection.commit()

print("Nouvel utilisateur ajouté !")

connection.close()