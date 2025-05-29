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