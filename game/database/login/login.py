#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3

connection = sqlite3.connect("../base.db")
cursor = connection.cursor()

pseudo = 'dsfsfs'
password = 'secdret'

query_pseudo = (pseudo,)

requete = cursor.execute('SELECT * FROM users WHERE username = ?', query_pseudo)
resultat = requete.fetchone()

if resultat != None:
    req_pseudo, req_password = resultat[1], resultat[2]

    if pseudo == req_pseudo and password == req_password:
        print("Login valide")
        # Passer Login a TRUE
    else:
        print("Login invalide")
        # Laisser Login a FALSE
else:
    # On stop tout
    pass

connection.close()