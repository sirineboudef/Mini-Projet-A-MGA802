from cesar import dechiffrer_texte


def charger_dictionnaire(fichier):
    # Ouvre le fichier en mode lecture avec l'encodage UTF-8
    with open(fichier, encoding='utf-8') as f:
        # Lit toutes les lignes du fichier et les stocke dans une liste (une ligne = un mot)
        mots = f.read().splitlines()

    # Convertit chaque mot en minuscules et les place dans un ensemble (set)
    # Cela permet d'éliminer les doublons et d'accélérer les recherches
    return set(m.lower() for m in mots)
