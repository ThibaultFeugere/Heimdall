#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3
import os.path


class Login:
    # Attribut

    # Initialisateur
    def __init__(self, pseudo, password):
        self.pseudo = pseudo
        self.password = password

    # Recupere pseudo/password BDD
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

    # Teste le pseudo et MDP
    def verify(self, resultat):
        if resultat != None:
            req_pseudo, req_password = resultat[1], resultat[2]
            if self.pseudo == req_pseudo and self.password == req_password:
                print("Login valide")
                # Passer Login a TRUE
            else:
                print("Login invalide")
                # Laisser Login a FALSE
        else:
            # On stop tout
            pass


# conn = Login('dfd', 'secdret')
# res = conn.fetchPseudo()
# conn.verify(res)
