import string

alphabet = "abcdefghijklmnopqrstuvwxyz"

def chiffrement_cesar(message, cle):
    message_crypte = ''
    # Convertir en minuscule pour gérer les majuscules
    for lettre in message.lower():
        # Crypter que les lettres de l'alphabet
        if lettre in alphabet:
            l = alphabet.find(lettre)
            l = (l + cle) % 26  # %26 assure que l'indice reste entre 0 et 25
            message_crypte += alphabet[l]
        else:
            # Garder les caractères non alphabétiques (espaces, ponctuation, etc)
            message_crypte += lettre

    return message_crypte

def dechiffrement_cesar(message, cle):
    message_decrypte = ''
    for lettre in message.lower():
        if lettre in alphabet:
            l = alphabet.find(lettre)
            l = (l - cle) % 26  # On soustrait k
            message_decrypte += alphabet[l]
        else:
            # Garde les caractères non alphabétiques
            message_decrypte += lettre

    return message_decrypte

def bruteforce(message):
    print("\n--- Mode Brute Force ---")
    for cle in range(1, 26):
        tentative = dechiffrement_cesar(message, cle)
        print(f"Clé {cle}: {tentative}")
    print("Essayez d’identifier visuellement le bon résultat.")




