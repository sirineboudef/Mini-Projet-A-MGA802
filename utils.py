# Importations necessaires
import unicodedata

# Definitions des lettres de l'alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Fonction pour enlever les caracteres speciaux
def enlever_caracteres_speciaux(texte):
    normalized_text = unicodedata.normalize('NFKD', texte)
    return ''.join([char for char in normalized_text if not unicodedata.combining(char)])

# Fonction pour lire un fichier
def lire_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Fichier {nom_fichier} introuvable.")
        return None
# Fonction pour ecrire un fichier
def ecrire_fichier(nom_fichier, contenu):
    with open(nom_fichier, 'w', encoding='utf-8') as f:
        f.write(contenu)

# Definitions des mots frequents
mots_frequents = {"le", "la", "et", "un", "de", "en", "est", "que", "dans", "pour"}

# Fonction pour charger le dictionnaire
def charger_dictionnaire(fichier):
    with open(fichier, encoding='utf-8') as f:
        mots = f.read().splitlines()
    return set(m.lower() for m in mots)



