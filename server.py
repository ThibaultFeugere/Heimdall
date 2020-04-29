import socket

# AF_INET = adresses Internet de type IPv4
# SOCK_STREAM = protocole TCP
socket_ecoute = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

adresse, port = ("192.168.1.4", 5555)

# On lie le socket à une adresse et un port
socket_ecoute.bind((adresse, port))

print("Le serveur est démarré")

while True:
    # On met le socket à l'état d'écoute sur le port bindé
    socket_ecoute.listen(5)

    # On accepte la connexion du client
    connexion_client, adresse_client = socket_ecoute.accept()

    # On attend de recevoir un message du serveur
    message = connexion_client.recv(1024)
    print(message)

# Fermeture des connexions
connexion_client.close()

# Fermeture du socket
socket_ecoute.close()
