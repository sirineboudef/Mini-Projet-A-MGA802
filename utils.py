# Importations necessaires
import unicodedata

# Definitions des lettres de l'alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Fonction pour enlever les caracteres speciaux
def enlever_caracteres_speciaux(texte):
    # Normalise le texte en forme 'NFKD', ce qui sépare les lettres des accents
    normalized_text = unicodedata.normalize('NFKD', texte)

    # Recompose le texte en supprimant les caractères "diacritiques" (accents, etc.)
    return ''.join([char for char in normalized_text if not unicodedata.combining(char)])

# Fonction pour lire un fichier
def lire_fichier(nom_fichier):
    try:
        # Ouvre le fichier en mode lecture texte avec l'encodage UTF-8
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        # Gère l'erreur si le fichier n'existe pas
        print(f"Fichier {nom_fichier} introuvable.")
        return None

# Fonction pour ecrire un fichier
def ecrire_fichier(nom_fichier, contenu):
    # Ouvre le fichier en mode écriture avec l'encodage UTF-8
    with open(nom_fichier, 'w', encoding='utf-8') as f:
        f.write(contenu)

# Definitions des mots frequents
mots_frequents = {"le", "la", "et", "un", "de", "en", "est", "que", "dans", "pour"}

# Fonction pour charger le dictionnaire
def charger_dictionnaire(fichier):
    with open(fichier, encoding='utf-8') as f:
        mots = f.read().splitlines()
    return set(m.lower() for m in mots)

# Fonction qui permet de demander le texte
def demander_texte():
    return input("Entrez le texte à traiter : ")

# Fonction qui permet d'avoir la cle
def demander_cle():
    while True:
        try:
            return int(input("Entrez la clé (positive ou négative) : "))
        except ValueError:
            print("Veuillez entrer un entier valide.")

# Fonction pour demander a l'utilisateur ou il veut avoir le resultat
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
