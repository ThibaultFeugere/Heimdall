def ask(connexion_with_serveur, Stop):
    # Demande de connexion ou d'enregistrement
    print("1 - Se connecter\n")
    print("2 - S'enregistrer\n")
    print("3 - Quitter\n")
    answer = input("Que souhaitez-vous faire (1, 2 ou 3) ?\n")

    # Connexion
    if answer == "1":
        return login(connexion_with_serveur)
    if answer == "2":
        return register(connexion_with_serveur)

    if answer == "3":
        print("Au revoir !")
        Stop.stop(connexion_with_serveur, False)

    if answer != "1" and answer != "2" and answer != "3":
        print("Nous n'avons pas compris...")
        ask(connexion_with_serveur, Stop)

def login(connexion_with_serveur):
    username = input("Quel est votre pseudo ?\n")
    password = input("Quel est votre mot de passe ?\n")
    connexion_with_serveur.sendall(("login, username," + username + ", password," + password).encode("utf8"))
    data = connexion_with_serveur.recv(1024)
    Login = data.decode("utf-8")
    if Login == "0":
        print("Login échoué, recommencez...")
        login(connexion_with_serveur)
    else:
        return True

def register(connexion_with_serveur):
    username = input("Quel est votre pseudo ?\n")
    password = input("Veuillez saisir un mot de passe\n")
    second_password = input("Veuillez resaisir le mot de passe\n")

    if password == second_password:
        connexion_with_serveur.sendall(("register, username," + username + ", password," + password).encode("utf8"))
        data = connexion_with_serveur.recv(1024)
        verify_register = data.decode("utf-8")
        if verify_register == "1":
            print("Vous pouvez désormais vous connecter...")
            login(connexion_with_serveur)
        if verify_register == "0":
            print("Le pseudo existe déjà...")
            return register(connexion_with_serveur)
    else:
        print("Les deux mot de passes ne correspondent pas...\n On recommence : \n")
        register(connexion_with_serveur)
