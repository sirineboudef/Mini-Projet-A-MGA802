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

from Affichage_pour_utilisateur import menu_principal

menu_principal()
