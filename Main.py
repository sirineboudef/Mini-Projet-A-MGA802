message = input("ecrit un message : ")

crypter = ""
decrypter = ""
alphabet ="abcdefghijklmnopqrstuvwxyz"
k=5

# Convertir en minuscule pour gérer les majuscules
for lettre in message.lower():
    # Crypter que les lettres de l'alphabet
    if lettre in alphabet:
        l = alphabet.find(lettre)
        l = (l + k) % 26  # %26 assure que l'indice reste entre 0 et 25
        crypter += alphabet[l]
    else:
        # Garder les caractères non alphabétiques (espaces, ponctuation, etc.)
        crypter += lettre

print(crypter)
message_chiffre = input("Écris le message à décrypter : ")

for lettre in message_chiffre.lower():
    if lettre in alphabet:
        l = alphabet.find(lettre)
        l = (l - k) % 26  # On soustrait k
        decrypter += alphabet[l]
    else:
        # Garde les caractères non alphabétiques
        decrypter += lettre

print(decrypter)