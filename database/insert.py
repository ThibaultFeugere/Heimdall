#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

connection = sqlite3.connect("base.db")
cursor = connection.cursor()

new_user = (cursor.lastrowid, "Jason", "secret")
cursor.execute('INSERT INTO users VALUES (?, ?, ?)', new_user)
connection.commit()

print("Nouvel utilisateur ajouté !")

connection.close()