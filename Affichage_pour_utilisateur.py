from cesar import*
from utils import lire_fichier, ecrire_fichier, charger_dictionnaire

def demander_texte():
    return input("Entrez le texte à traiter : ")

def demander_cle():
    while True:
        try:
            return int(input("Entrez la clé (positive ou négative) : "))
        except ValueError:
            print("Veuillez entrer un entier valide.")

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


def menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Chiffrer un texte")
        print("2. Déchiffrer un texte")
        print("3. Chiffrer un fichier")
        print("4. Déchiffrer un fichier")
        print("5. Déchiffrer un texte sans clé")
        print("6. Quitter")

        choix = input("Votre choix : ")

        if choix == '1':
            texte = demander_texte()
            cle = demander_cle()
            sortie = demander_sortie()
            if sortie == '1':
                print("\nTexte chiffré :", chiffrer_texte(texte, cle))
            else:
                nom_fichier = input("Nom du fichier de sortie : ")
                nom_fichier =f"{nom_fichier}.txt"
                ecrire_fichier(nom_fichier, chiffrer_texte(texte, cle))
                print(f"Résultat enregistré dans {nom_fichier}")

        elif choix == '2':
            texte = demander_texte()
            cle = demander_cle()
            sortie = demander_sortie()
            if sortie == '1':
                print("\nTexte déchiffré :", dechiffrer_texte(texte, cle))
            else:
                nom_fichier = input("Nom du fichier de sortie : ")
                nom_fichier = f"{nom_fichier}.txt"
                ecrire_fichier(nom_fichier, dechiffrer_texte(texte, cle))
                print(f"Résultat enregistré dans {nom_fichier}")

        elif choix == '3':
            nom = input("Nom du fichier à chiffrer : ")
            contenu = lire_fichier(nom)
            if contenu:
                cle = demander_cle()
                resultat = chiffrer_texte(contenu, cle)
                nom_sortie = input("Nom du fichier de sortie (ex: mon_fichier_chiffre.txt) : ")
                ecrire_fichier(nom_sortie, resultat)
                print(f"Fichier chiffré enregistré dans {nom_sortie}")

        elif choix == '4':
            nom = input("Nom du fichier à déchiffrer : ")
            contenu = lire_fichier(nom)
            if contenu:
                cle = demander_cle()
                resultat = dechiffrer_texte(contenu, cle)
                nom_sortie = input("Nom du fichier de sortie (ex: mon_fichier_dechiffre.txt) : ")
                ecrire_fichier(nom_sortie, resultat)
                print(f"Fichier déchiffré enregistré dans {nom_sortie}")

        elif choix == "5":
            # Chargement du dictionnaire
            dico = charger_dictionnaire("ressources/dico.txt")
            texte = demander_texte()

            # Mots fréquents (tu peux aussi les charger depuis un fichier si besoin)

            mots_frequents = {"le", "la", "et", "un", "de", "en", "est", "que", "dans", "pour"}

            # Appel du déchiffrement intelligent (avec interaction utilisateur)

            texte_final, cle = dechiffrer_automatiquement(texte, mots_frequents, dico)

            if texte_final:

                print("\n Texte déchiffré :", texte_final)

                print(" Clé trouvée :", cle)

            else:

                print("\n Aucune proposition n’a été validée par l’utilisateur.")

        elif choix == '6':
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")