
"""Ce module inclus toutes les fonction necessaires a l'execution de la methode
de la brute-force automatique"""
# 1- Compter le nombre de mots frequents contenu dans le texte.
# 2- Tester les cles et ne garder que celles qui ont un nombre de mots superieur ou egale a 3
# 3- Etude des differents cas:
# - Si il ya une seule meilleure cle dechiffre et donner le resultat.
# - Si il n'ya aucune meilleure cle faire le teste de toutes les cles a travers le dictionnaire.
# - Si il ya plusieurs meilleures cles dechifferer avec la cle qui possede le meilleur score (plus de mots frequents)
# - Si il ya plusieurs meilleures cles avec le meme score le teste de ces cles a travers le dictionnaire.

""" Cela permet d'éviter de perdre du temps a essayer toutes les cles possible directement a traves
le dictionnaire, et tenter d'abord d'explorer une liste de mot frequents """

# Importations necessaires
import string
from chiffrement_cesar import* # Importer tous ce qu'il ya dans cesar

SEUIL_MIN=3  # score minimal pour considérer un score valable

# Fonction pour compter combien de mots frequents sont utilisés dans le texte/fichier
def compter_mots_frequents(texte, liste_mots):
    mots = texte.lower().translate(str.maketrans('', '', string.punctuation)).split()
    return sum(1 for mot in mots if mot in liste_mots)

# Fonction pour tester les cles et les valider.
def tester_cles(texte, cles_a_tester, dictionnaire):
    scores = []
    for cle in cles_a_tester:
        texte_dechiffre = dechiffrer_texte(texte, cle)
        score = compter_mots_frequents(texte_dechiffre, dictionnaire)
        if score >= SEUIL_MIN:
            scores.append((cle, texte_dechiffre, score))

    # Trier les résultats par score décroissant
    scores.sort(key=lambda x: x[2], reverse=True)
    # Permettre a l'utilisateur de valider a la fin
    for cle, texte_dechiffre, score in scores:
        print(f"\n Proposition avec la clé {cle} (score: {score}) :")
        print(texte_dechiffre)
        if  input(" Ce texte vous semble correct ? (o/n) : ").strip().lower()=='o':
            print("Texte validé par l'utilisateur.")
            return texte_dechiffre, cle
    return None, None

# Méthode automatique principale avec validation utilisateur
def dechiffrer_automatiquement(texte, liste_mots, dictionnaire):
    scores = {cle: compter_mots_frequents(dechiffrer_texte(texte, cle), liste_mots) for cle in range(26)}
    max_score = max(scores.values())
    meilleures_cles = [cle for cle, score in scores.items() if score == max_score]

    # Cas 1 : aucun mot fréquent → test complet avec dictionnaire
    if max_score == 0:
        return tester_cles(texte, range(26), dictionnaire)

    # Cas 2 : une seule clé se détache et donc donner le resultats sans perdre du temps
    if len(meilleures_cles) == 1:
        cle = meilleures_cles[0]
        candidat = dechiffrer_texte(texte, cle)
        if compter_mots_frequents(candidat, liste_mots) >= SEUIL_MIN:
            print(f"\n Clé probable détectée : {cle}")
            print(candidat)
            if input(" Ce texte vous semble correct ? (o/n) : ").strip().lower() == 'o':
                return candidat, cle
        return tester_cles(texte, [c for c in range(26) if c != cle], dictionnaire)

    # Cas 3 : plusieurs clés avec même score (affiner avec dictionnaire)
    return tester_cles(texte, meilleures_cles, dictionnaire)


