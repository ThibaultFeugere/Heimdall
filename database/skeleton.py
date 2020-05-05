#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

try:
    connection = sqlite3.connect("base.db")
    cursor = connection.cursor()

    pseudo = ('thibault',)

    requete = cursor.execute('SELECT * FROM users WHERE username = ?', pseudo)
    resultat = requete.fetchone()
    username = resultat[1]

    print(resultat, username)
except Exception as e:
    print("ERREUR : ", e)
    connection.rollback()
finally:
    connection.close()