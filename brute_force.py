import string
from cesar import*

# fonction qui fait le decompte des mots les plus utilises en langue francaise
def compter_mots_frequents(texte, mots_frequents):
    mots = texte.lower().translate(str.maketrans('', '', string.punctuation)).split()
    return sum(1 for mot in mots if mot in mots_frequents)