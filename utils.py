def lire_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Fichier {nom_fichier} introuvable.")
        return None

def ecrire_fichier(nom_fichier, contenu):
    with open(nom_fichier, 'w', encoding='utf-8') as f:
        f.write(contenu)