#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3
import os.path


class All:

    # Initialisateur
    def __init__(self, username):
        self.username = username

    # Recupere pseudo/password BDD
    def fetch_all(self):
        query_pseudo = (self.username,)
        path_db = os.path.join(os.path.dirname(
            os.path.abspath(__file__))) + './base.db'
        connection = sqlite3.connect(path_db)
        cursor = connection.cursor()
        requete = cursor.execute(
            'SELECT * FROM users WHERE username = ?', query_pseudo)
        resultat = requete.fetchone()
        connection.close()
        return resultat
