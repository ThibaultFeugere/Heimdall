#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3
import os.path
from datetime import datetime


class Register():

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register(self):
        path_db = os.path.join(os.path.dirname(
            os.path.abspath(__file__))) + '/../base.db'
        connection = sqlite3.connect(path_db)
        cursor = connection.cursor()
        query_pseudo = (self.username,)
        requete = cursor.execute(
            'SELECT * FROM users WHERE username = ?', query_pseudo)
        resultat = requete.fetchone()
        cursor.close()
        if resultat == None:
            cursor = connection.cursor()
            new_user = (cursor.lastrowid, self.username, self.password,
                        100, datetime.now(), datetime.now())
            cursor.execute(
                'INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)', new_user)
            connection.commit()
            return True
        connection.close()
        return False
