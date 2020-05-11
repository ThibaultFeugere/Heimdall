#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3
from datetime import datetime

connection = sqlite3.connect("../base.db")
cursor = connection.cursor()

pseudo = 'dddddddddd'
password = 'secdresssst'

query_pseudo = (pseudo,)

requete = cursor.execute('SELECT * FROM users WHERE username = ?', query_pseudo)
resultat = requete.fetchone()
cursor.close()

if resultat == None:
    cursor = connection.cursor()
    new_user = (cursor.lastrowid, pseudo, password, 100, datetime.now(), datetime.now())
    cursor.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)', new_user)
    connection.commit()
    print("Utilisateur ajouté")
else:
    print("Pseudo existe deja")


connection.close()