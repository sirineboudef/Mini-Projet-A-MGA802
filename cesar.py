import string
from utils import enlever_caracteres_speciaux
from charset_normalizer.utils import remove_accent

alphabet = "abcdefghijklmnopqrstuvwxyz"

def chiffrer_texte(texte, cle):
    texte_sans_accent = enlever_caracteres_speciaux(texte)
    texte_crypte = ''
    # Convertir en minuscule pour gérer les majuscules
    for lettre in texte_sans_accent.lower():
        # Crypter que les lettres de l'alphabet
        if lettre in alphabet:
            l = alphabet.find(lettre)
            l = (l + cle) % 26  # %26 assure que l'indice reste entre 0 et 25
            texte_crypte += alphabet[l]
        else:
            # Garder les caractères non alphabétiques (espaces, ponctuation, etc)
            texte_crypte += lettre

    return texte_crypte

def dechiffrer_texte(texte, cle):
    texte_sans_accent = enlever_caracteres_speciaux(texte)
    texte_decrypte = ''
    for lettre in texte_sans_accent.lower():
        if lettre in alphabet:
            l = alphabet.find(lettre)
            l = (l - cle) % 26  # On soustrait k
            texte_decrypte += alphabet[l]
        else:
            # Garde les caractères non alphabétiques
            texte_decrypte += lettre

    return texte_decrypte

def bruteforce(texte):
    print("\n--- Mode Brute Force ---")
    for cle in range(1, 26):
        tentative = dechiffrer_texte(texte, cle)
        print(f"Clé {cle}: {tentative}")
    print("Essayez d’identifier visuellement le bon résultat.")




