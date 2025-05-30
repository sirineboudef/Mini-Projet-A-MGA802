import string
from cesar import*

# Fonction pour le decompte des mots les plus utilises en langue francaise
def compter_mots_frequents(texte, mots_frequents):
    mots = texte.lower().translate(str.maketrans('', '', string.punctuation)).split()
    return sum(1 for mot in mots if mot in mots_frequents)

# Fonction pour tester les cles et les valider.
def tester_cles_et_valider(texte, cles_a_tester, dictionnaire):
    scores = []
    for cle in cles_a_tester:
        texte_dechiffre = dechiffrer_texte(texte, cle)
        mots = texte_dechiffre.lower().translate(str.maketrans('', '', string.punctuation)).split()
        score = sum(1 for mot in mots if mot in dictionnaire)
        scores.append((cle, texte_dechiffre, score))
# Trier les résultats par score décroissant
    scores.sort(key=lambda x: x[2], reverse=True)

    for cle, texte_propose, score in scores:
        print(f"\n Proposition avec la clé {cle} (score: {score}) :")
        print(texte_propose)
        reponse = input(" Ce texte vous semble correct ? (o/n) : ").strip().lower()
        if reponse == 'o':
            print("Texte validé par l'utilisateur.")
            return texte_propose, cle

    print(" Aucun texte n'a été validé par l'utilisateur ")
    return None, None

# Méthode automatique principale avec validation utilisateur
def dechiffrer_automatiquement(texte, mots_frequents, dictionnaire):
    scores_frequents = {}
    for cle in range(26):
        texte_dechiffre = dechiffrer_texte(texte, cle)
        score = compter_mots_frequents(texte_dechiffre, mots_frequents)
        scores_frequents[cle] = score

    max_score = max(scores_frequents.values())
    meilleures_cles = [cle for cle, score in scores_frequents.items() if score == max_score]

    if max_score == 0:
        return tester_cles_et_valider(texte, range(26), dictionnaire)
    elif len(meilleures_cles) == 1:
        texte_propose = dechiffrer_texte(texte, meilleures_cles[0])
        print(f"\n Clé la plus probable détectée : {meilleures_cles[0]}")
        print(texte_propose)
        reponse = input(" Ce texte vous semble correct ? (o/n) : ").strip().lower()
        if reponse == 'o':
            return texte_propose, meilleures_cles[0]
        else:
            # Si refusé, on essaie les autres clés classées
            return tester_cles_et_valider(texte, [cle for cle in range(26) if cle != meilleures_cles[0]], dictionnaire)
    else:
        return tester_cles_et_valider(texte, meilleures_cles, dictionnaire)
from cesar import dechiffrer_texte

def charger_dictionnaire(fichier):
    with open(fichier, encoding='utf-8') as f:
        mots = f.read().splitlines()
    return set(m.lower() for m in mots)

def bruteforce_texte(texte, dictionnaire):
    meilleur_score = 0
    meilleure_cle = None
    meilleur_texte = ""

    for cle in range(1, 26):
        texte = dechiffrer_texte(texte, cle)
        mots = texte.lower().split()
        score = sum(1 for mot in mots if mot.strip(",.!?;:") in dictionnaire)

        if score > meilleur_score:
            meilleur_score = score
            meilleure_cle = cle
            meilleur_texte = texte

    return meilleure_cle, meilleur_texte
