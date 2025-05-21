message = input("ecrit un message : ")

crypter = ""
decrypter = ""
alphabet ="abcdefghijklmnopqrstuvwxyz"
k=5

for lettre in message.lower():  # Convertir en minuscule pour gérer les majuscules
    if lettre in alphabet:  # Ne crypter que les lettres de l'alphabet
        l = alphabet.find(lettre)
        l = (l + k) % 26  # %26 assure que l'indice reste entre 0 et 25
        crypter += alphabet[l]
    else:
        crypter += lettre  # Garder les caractères non alphabétiques (espaces, ponctuation, etc.)

print(crypter)
message_chiffre = input("Écris le message à décrypter : ")

for lettre in message_chiffre.lower():
    if lettre in alphabet:
        l = alphabet.find(lettre)
        l = (l - k) % 26  # On soustrait k
        decrypter += alphabet[l]
    else:
        decrypter += lettre  # Garde les caractères non alphabétiques

print(decrypter)