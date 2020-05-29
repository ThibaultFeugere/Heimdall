# Documentation

Pour pouvoir jouer au jeu, vous devez installer pygame avec la commande : `pip install pygame`

## Serveur

Le `server.py` s'occupe de lancer le serveur et de gérer les threads. Celui-ci écoute sur un port précis et, lors d'une connexion, s'occupe aussi de générer un thread pour communiquer avec le jeu.
Il est indispensable de lancer le `server.py` avant de lancer le client (`main.py`)

### Login

`login.py` est la classe permettant de vérifier si l'utilisateur existe et si le mot de passe est correcte, côté serveur. Ensuite, le serveur donne une réponse positive ou négative au client.

### Register

`register.py` est la classe permettant de vérifier si l'utilisateur existe ou non et crée le compte dans la base de données, puis envoi une réponse.

## Client

Le `main.py` est en quelque sorte l'orchestrateur de nombreux morceaux du code permettant :
- de se connecter et communiquer au serveur
- d'accéder au menu
- d'accéder aux statistiques
- de lancer un combat
- d'acheter dans la boutique

### Buttons

Buttons est la partie ou nous stockons la gestion de tous nos bouttons afin de gérer l'affichage mais aussi les coordonnées de clics afin de savoir ce que l'utilisateur sélectionne. Une fonction custom a été développée pour que nous puissions rajouter des bouttons avec le texte souhaité de manière très rapide. C'est en quelque sorte un `helper`.

### Player

Player est la classe qui nous permet d'instancier un joueur lors du lancement du jeux. Celle-ci possède différents attributs :

- Max_health (PV Max)
- Health (PV actuel)
- Damage (Dégats qu'on inflige au Bot)
- Level (Niveau actuel)
- Win (Nombre de victoires)
- Lose (Nombre de défaites)
- Money (Nombre de PO)
- Heal (Nombre de PV restaurés)
- Potions (Nombre de potions)
- Image

### Bot

Bot est la classe qui nous permet d'instancier un adversaire face au Player. Celle-ci possède différents attributs

- Max_health (PV Max)
- Health (PV actuel)
- Damage (Dégats qu'on inflige au Bot)
- Image

### Stop

Stop est un fichier ou nous stockons les lignes récurrentes lors de l'arrêt du jeu. On peut spécifier l'arrêt de la musique ou non

### Credentials

`credentials.py` est la partie qui gère la connexion et la communication du client vers le serveur. Le système se veut récursif.
