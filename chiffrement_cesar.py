# Importations necessaires: importer tous ce qu'il ya dans utils
from utils import*

# Fonction qui sert a chiffrer un texte a partir d'une cle
def chiffrer_texte(texte, cle):
    texte_sans_accent = enlever_caracteres_speciaux(texte)
    texte_crypte = ''
    # Convertir en minuscule pour gérer les majuscules
    for lettre in texte_sans_accent.lower():
        # Chiffrer que les lettres de l'alphabet
        if lettre in alphabet:
            l = alphabet.find(lettre)
            l = (l + cle) % 26  # %26 assure que l'indice reste entre 0 et 25
            texte_crypte += alphabet[l]
        else:
            # Garder les caractères non alphabétiques (espaces, ponctuation, etc)
            texte_crypte += lettre

    return texte_crypte

# Fonction qui sert a dechiffrer un texte avec cle
def dechiffrer_texte(texte, cle):
    texte_sans_accent = enlever_caracteres_speciaux(texte)
    texte_decrypte = ''
    # Convertir en minuscule pour gérer les majuscules
    for lettre in texte_sans_accent.lower():
        # Chiffrer que les lettres de l'alphabet
        if lettre in alphabet:
            l = alphabet.find(lettre)
            l = (l - cle) % 26  # On soustrait k
            texte_decrypte += alphabet[l]
        else:
            # Garde les caractères non alphabétiques
            texte_decrypte += lettre

    return texte_decrypte





