import string

alphabet = string.ascii_lowercase

def chiffrement_cesar(message, cle):
    resultat = ''
    for char in message:
        if char.lower() in alphabet:
            idx = alphabet.find(char.lower())
            new_idx = (idx + cle) % 26
            new_char = alphabet[new_idx]
            if char.isupper():
                resultat += new_char.upper()
            else:
                resultat += new_char
        else:
            resultat += char
    return resultat

def dechiffrement_cesar(message, cle):
    return chiffrement_cesar(message, -cle)

def bruteforce(message):
    print("\n--- Mode Brute Force ---")
    for cle in range(1, 26):
        tentative = dechiffrement_cesar(message, cle)
        print(f"Clé {cle}: {tentative}")
    print("Essayez d’identifier visuellement le bon résultat.")
