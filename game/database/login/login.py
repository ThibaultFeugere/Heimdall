#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3
import os.path


class Login:
    # Attribut

    # Initialisateur
    def __init__(self, pseudo, password):
        self.pseudo = 'dfd'
        self.password = 'secdret'

    def fetchPseudo(self):
        query_pseudo = (self.pseudo,)  # mise en tuple
        path_db = os.path.join(os.path.dirname(
            os.path.abspath(__file__))) + '/../base.db'
        connection = sqlite3.connect(path_db)
        cursor = connection.cursor()
        requete = cursor.execute(
            'SELECT * FROM users WHERE username = ?', query_pseudo)
        resultat = requete.fetchone()
        connection.close()
        return resultat

    def verify(self, resultat):
        if resultat != None:
            req_pseudo, req_password = resultat[1], resultat[2]
            if self.pseudo == req_pseudo and self.password == req_password:
                return "Login valide"
                # Passer Login a TRUE
            else:
                return "Login invalide"
                # Laisser Login a FALSE
        else:
            # On stop tout
            pass


# conn = Login('test', 'test')
# res = conn.fetchPseudo()
# print(res)
# print(conn.verify(res))
