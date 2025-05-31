"""
Programme de chiffrement et déchiffrement avec le chiffrement de César
-----------------------------------------------------------------------

Ce programme permet à l'utilisateur de :
- Chiffrer un message avec une clé (positive ou négative)
- Déchiffrer un message avec une clé connue
- Appliquer un déchiffrement automatique (brute force) sans connaître la clé
- Chiffrer ou déchiffrer le contenu d’un fichier texte
- Enregistrer les résultats dans un fichier ou les afficher à l’écran

Modules requis : cesar.py (algorithmes de chiffrement), utils.py (lecture/écriture de fichiers)

Auteurs : Alexis Chenuet  
          Syrine Boudef  
          Wilson David Parra Oliveros
"""

from brute_force import*
from chiffrement_cesar import*

# Fonction principale du programme
def menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Chiffrer un texte")
        print("2. Déchiffrer un texte")
        print("3. Chiffrer un fichier")
        print("4. Déchiffrer un fichier")
        print("5. Déchiffrer un texte sans clé")
        print("6. Déchiffrer un fichier sans clé")
        print("7. Quitter")

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
            dico = charger_dictionnaire("ressources/dico.txt")
            texte = demander_texte()
            texte_final, cle = dechiffrer_automatiquement(texte, mots_frequents, dico)

            if texte_final and cle is not None:
                choix = demander_sortie()
                if choix == '1':
                    print("\nTexte déchiffré :")
                    print(texte_final)
                    print(f"Clé trouvée : {cle}")
                elif choix=='2':
                    nom_fichier = input("Nom du fichier de sortie : ")
                    contenu = f"Clé trouvée : {cle}\n\nTexte déchiffré :\n{texte_final}"
                    ecrire_fichier(nom_fichier, contenu)
                    print(f"\nRésultat enregistré dans {nom_fichier}")
            else:
                print("\n Aucune proposition n’a été validée par l’utilisateur.")

        elif choix == "6":
            dico = charger_dictionnaire("ressources/dico.txt")
            nom_fichier = input("Nom du fichier à déchiffrer : ")
            texte = lire_fichier(nom_fichier)
            if texte:
                texte_final, cle = dechiffrer_automatiquement(texte, mots_frequents, dico)
                if texte_final and cle is not None:
                    sortie = demander_sortie()
                    if sortie == '1':
                        print("\nTexte déchiffré :")
                        print(texte_final)
                        print(f"Clé trouvée : {cle}")
                    else:
                        nom_fichier = input("Nom du fichier de sortie : ")
                        contenu = f"Clé trouvée : {cle}\n\nTexte déchiffré :\n{texte_final}"
                        ecrire_fichier(nom_fichier, contenu)
                        print(f"\nRésultat enregistré dans {nom_fichier}")
                else:
                    print("\nAucune proposition n’a été validée par l’utilisateur.")

        elif choix == '7':
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")

menu_principal()
