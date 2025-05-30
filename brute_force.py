import string
from cesar import*
SEUIL_MIN=3  # score minimal pour considérer une proposition valable

# Fonction pour le decompte des mots les plus utilises en langue francaise
def compter_mots_frequents(texte, mots_frequents):
    mots = texte.lower().translate(str.maketrans('', '', string.punctuation)).split()
    return sum(1 for mot in mots if mot in mots_frequents)

# Fonction pour tester les cles et les valider.
def tester_cles(texte, cles_a_tester, dictionnaire):
    scores = []
    for cle in cles_a_tester:
        texte_dechiffre = dechiffrer_texte(texte, cle)
        mots = texte_dechiffre.lower().translate(str.maketrans('', '', string.punctuation)).split()
        score = compter_mots_frequents(texte_dechiffre, dictionnaire)
        if score >= SEUIL_MIN:
            scores.append((cle, texte_dechiffre, score))


# Trier les résultats par score décroissant
    scores.sort(key=lambda x: x[2], reverse=True)

    for cle, texte_dechiffre, score in scores:
        print(f"\n Proposition avec la clé {cle} (score: {score}) :")
        print(texte_dechiffre)
        if  input(" Ce texte vous semble correct ? (o/n) : ").strip().lower()=='o':
            print("Texte validé par l'utilisateur.")
            return texte_dechiffre, cle

    print(" Aucun texte n'a été validé par l'utilisateur ")
    return None, None


# Méthode automatique principale avec validation utilisateur
def dechiffrer_automatiquement(texte, mots_frequents, dictionnaire):
    scores = {cle: compter_mots_frequents(dechiffrer_texte(texte, cle), mots_frequents) for cle in range(26)}
    max_score = max(scores.values())
    meilleures_cles = [cle for cle, score in scores.items() if score == max_score]

    # Cas 1 : aucun mot fréquent → test complet avec dictionnaire
    if max_score == 0:
        return tester_cles(texte, range(26), dictionnaire)

    # Cas 2 : une seule clé se détache
    if len(meilleures_cles) == 1:
        cle = meilleures_cles[0]
        candidat = dechiffrer_texte(texte, cle)
        if compter_mots_frequents(candidat, mots_frequents) >= SEUIL_MIN:
            print(f"\n🔑 Clé probable détectée : {cle}")
            print(candidat)
            if input("✅ Ce texte vous semble correct ? (o/n) : ").strip().lower() == 'o':
                return candidat, cle
        return tester_cles(texte, [c for c in range(26) if c != cle], dictionnaire)

    # Cas 3 : plusieurs clés avec même score → affiner avec dictionnaire
    return tester_cles(texte, meilleures_cles, dictionnaire)
