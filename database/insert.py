#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
from datetime import datetime

connection = sqlite3.connect("base.db")
cursor = connection.cursor()

new_user = (cursor.lastrowid, "Jason", "secret", datetime.now(), datetime.now())
cursor.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?)', new_user)
connection.commit()

print("Nouvel utilisateur ajouté !")

connection.close()