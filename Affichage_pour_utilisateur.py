from cesar import chiffrement_cesar, dechiffrement_cesar, bruteforce
from utils import lire_fichier, ecrire_fichier

def demander_texte():
    return input("Entrez le texte à traiter : ")

def demander_cle():
    while True:
        try:
            return int(input("Entrez la clé (positive ou négative) : "))
        except ValueError:
            print("Veuillez entrer un entier valide.")

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

        if choix == '1':
            message = demander_texte()
            cle = demander_cle()
            print("Message chiffré :", chiffrement_cesar(message, cle))
        elif choix == '2':
            message = demander_texte()
            cle = demander_cle()
            print("Message déchiffré :", dechiffrement_cesar(message, cle))
        elif choix == '3':
            nom = input("Nom du fichier à chiffrer : ")
            contenu = lire_fichier(nom)
            if contenu:
                cle = demander_cle()
                resultat = chiffrement_cesar(contenu, cle)
                ecrire_fichier("fichier_chiffre.txt", resultat)
                print("Fichier chiffré dans fichier_chiffre.txt")
        elif choix == '4':
            nom = input("Nom du fichier à déchiffrer : ")
            contenu = lire_fichier(nom)
            if contenu:
                cle = demander_cle()
                resultat = dechiffrement_cesar(contenu, cle)
                ecrire_fichier("fichier_dechiffre.txt", resultat)
                print("Fichier déchiffré dans fichier_dechiffre.txt")
        elif choix == '5':
            message = demander_texte()
            bruteforce(message)
        elif choix == '6':
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")