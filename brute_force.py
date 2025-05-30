from cesar import dechiffrer_texte


def charger_dictionnaire(fichier):
    # Ouvre le fichier en mode lecture avec l'encodage UTF-8
    with open(fichier, encoding='utf-8') as f:
        # Lit toutes les lignes du fichier et les stocke dans une liste (une ligne = un mot)
        mots = f.read().splitlines()

    # Convertit chaque mot en minuscules et les place dans un ensemble (set)
    # Cela permet d'éliminer les doublons et d'accélérer les recherches
    return set(m.lower() for m in mots)

def bruteforce_texte(texte, dictionnaire):
    # Initialiser les variables pour garder la meilleure clé, le meilleur score et le meilleur texte
    meilleur_score = 0
    meilleure_cle = None
    meilleur_texte = ""

    # Essayer toutes les clés possibles de 1 à 25 (chiffrement de César)
    for cle in range(1, 26):
        # Déchiffrer le texte avec la clé actuelle
        texte = dechiffrer_texte(texte, cle)

        # Mettre le texte en minuscules et le découper en mots
        mots = texte.lower().split()

        # Calculer un "score" : le nombre de mots qui existent dans le dictionnaire
        # On retire la ponctuation de fin des mots avec strip
        score = sum(1 for mot in mots if mot.strip(",.!?;:") in dictionnaire)

        # Si ce score est meilleur que les précédents, on met à jour les meilleurs résultats
        if score > meilleur_score:
            meilleur_score = score
            meilleure_cle = cle
            meilleur_texte = texte

    # Retourner la clé et le texte déchiffré avec le meilleur score
    return meilleure_cle, meilleur_texte
