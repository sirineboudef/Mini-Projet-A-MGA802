# Importation des fonctions nécessaires depuis les fichiers modules
from cesar import chiffrement_cesar, dechiffrement_cesar, bruteforce
from utils import lire_fichier, ecrire_fichier

# Fonction pour demander un texte à l'utilisateur
def demander_texte():
    return input("Entrez le texte à traiter : ")

# Fonction pour demander une clé et s'assurer qu'elle soit un entier
def demander_cle():
    while True:
        try:
            return int(input("Entrez la clé (positive ou négative) : "))
        except ValueError:
            print("Veuillez entrer un entier valide.")

# Fonction pour choisir où afficher le résultat (console ou fichier)
def demander_sortie():
    """Demande à l'utilisateur où il veut voir le résultat"""
    while True:
        print("\nOù voulez-vous le résultat ?")
        print("1. Afficher dans la console")
        print("2. Enregistrer dans un fichier")
        choix = input("Votre choix : ")
        if choix in ('1', '2'):
            return choix
        print("Choix invalide.")


# Menu principal du programme
def menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Chiffrer un message")
        print("2. Déchiffrer un message")
        print("3. Chiffrer un fichier")
        print("4. Déchiffrer un fichier")
        print("5. Décrypter sans clé (Brute force)")
        print("6. Quitter")

        choix = input("Votre choix : ")

        # Option 1 : Chiffrement manuel d'un message
        if choix == '1':
            message = demander_texte()
            cle = demander_cle()
            sortie = demander_sortie()
            if sortie == '1':
                print("\nMessage chiffré :", chiffrement_cesar(message, cle))
            else:
                nom_fichier = input("Nom du fichier de sortie : ")
                nom_fichier =f"{nom_fichier}.txt"
                ecrire_fichier(nom_fichier, chiffrement_cesar(message, cle))
                print(f"Résultat enregistré dans {nom_fichier}")

        # Option 2 : Déchiffrement manuel d’un message
        elif choix == '2':
            message = demander_texte()
            cle = demander_cle()
            sortie = demander_sortie()
            if sortie == '1':
                print("\nMessage déchiffré :", dechiffrement_cesar(message, cle))
            else:
                nom_fichier = input("Nom du fichier de sortie : ")
                nom_fichier = f"{nom_fichier}.txt"
                ecrire_fichier(nom_fichier, dechiffrement_cesar(message, cle))
                print(f"Résultat enregistré dans {nom_fichier}")

        # Option 3 : Chiffrement d’un fichier texte
        elif choix == '3':
            nom = input("Nom du fichier à chiffrer : ")
            contenu = lire_fichier(nom)
            if contenu:
                cle = demander_cle()
                resultat = chiffrement_cesar(contenu, cle)
                nom_sortie = input("Nom du fichier de sortie (ex: mon_fichier_chiffre.txt) : ")
                ecrire_fichier(nom_sortie, resultat)
                print(f"Fichier chiffré enregistré dans {nom_sortie}")

        # Option 4 : Déchiffrement d’un fichier texte
        elif choix == '4':
            nom = input("Nom du fichier à déchiffrer : ")
            contenu = lire_fichier(nom)
            if contenu:
                cle = demander_cle()
                resultat = dechiffrement_cesar(contenu, cle)
                nom_sortie = input("Nom du fichier de sortie (ex: mon_fichier_dechiffre.txt) : ")
                ecrire_fichier(nom_sortie, resultat)
                print(f"Fichier déchiffré enregistré dans {nom_sortie}")

        # Option 5 : Décryptage automatique sans connaître la clé (brute force)
        elif choix == '5':
            message = demander_texte()
            bruteforce(message)

        # Option 6 : Quitter le programme
        elif choix == '6':
            print("Au revoir, a la prochaine!")
            break
        # Gestion des entrées invalides
        else:
            print("Choix invalide.")