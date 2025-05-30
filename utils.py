import unicodedata  # Module pour manipuler les caractères Unicode

# Fonction pour supprimer les caractères accentués (é, è, à → e, e, a)
def enlever_caracteres_speciaux(texte):
    # Normalise le texte en forme 'NFKD', ce qui sépare les lettres des accents
    normalized_text = unicodedata.normalize('NFKD', texte)

    # Recompose le texte en supprimant les caractères "diacritiques" (accents, etc.)
    return ''.join([char for char in normalized_text if not unicodedata.combining(char)])


# Fonction pour lire le contenu d’un fichier texte
def lire_fichier(nom_fichier):
    try:
        # Ouvre le fichier en mode lecture texte avec l'encodage UTF-8
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        # Gère l'erreur si le fichier n'existe pas
        print(f"Fichier {nom_fichier} introuvable.")
        return None

# Fonction pour écrire du contenu dans un fichier texte
def ecrire_fichier(nom_fichier, contenu):
    # Ouvre le fichier en mode écriture avec l'encodage UTF-8
    with open(nom_fichier, 'w', encoding='utf-8') as f:
        f.write(contenu)


