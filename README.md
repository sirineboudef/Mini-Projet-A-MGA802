
# Mini-Projet-A-MGA802
Création d'un programme de chiffrement de cesar

## Fonctionnalités du programme

Ce programme permet à l'utilisateur de :

1. **Chiffrer ou déchiffrer du texte**  
   - Le texte peut être introduit **par la console** ou **depuis un fichier**.  
   - L'utilisateur peut choisir d'obtenir le résultat **dans la console** ou **enregistré dans un fichier**.

2. **Déchiffrer un texte par la méthode de la force brute automatique**  
   - Le texte peut également être introduit **par la console** ou **depuis un fichier**.  
   - Le résultat peut être affiché **dans la console** ou **enregistré dans un fichier**, selon le choix de l'utilisateur.


### 1. Chiffrer un texte
- **Étapes :**
  1. L'utilisateur saisit le texte à chiffrer
  2. L'utilisateur entre la clé de chiffrement (entier positif ou négatif)
  3. Choix de sortie :
     - **Option 1** : Affichage du message chiffré dans la console
     - **Option 2** : Enregistrement dans un fichier texte (nom personnalisable)

### 2. Déchiffrer un texte
- **Étapes :**
  1. L'utilisateur saisit le texte chiffré
  2. L'utilisateur entre la clé de déchiffrement
  3. Choix de sortie :
     - **Option 1** : Affichage du message déchiffré dans la console
     - **Option 2** : Enregistrement dans un fichier texte (nom personnalisable)

### 3. Chiffrer un fichier
- **Étapes :**
  1. L'utilisateur spécifie le fichier source à chiffrer
  2. L'utilisateur entre la clé de chiffrement
  3. Le système génère un nouveau fichier chiffré avec :
     - Nom personnalisable par l'utilisateur
     - Extension `.txt` automatique

### 4. Déchiffrer un fichier
- **Étapes :**
  1. L'utilisateur spécifie le fichier chiffré à décoder
  2. L'utilisateur entre la clé de déchiffrement
  3. Le système génère un nouveau fichier déchiffré avec :
     - Nom personnalisable par l'utilisateur
     - Extension `.txt` automatique
     - 
### 5. Déchiffrer un texte avec brute-force
- **Étapes :**
  1. L'utilisateur saisit le texte à chiffrer
  2. L'utilisateur doit valider le resultat ou pas
  3. Choix de sortie :
     - **Option 1** : Affichage du message chiffré dans la console
     - **Option 2** : Enregistrement dans un fichier texte (nom personnalisable)
     - 
### 4. Déchiffrer un fichier avec brute force
- **Étapes :**
  1. L'utilisateur spécifie le fichier chiffré à décoder
  2. L'utilisateur valide le resultat ou pas
  3. Choix de sortie :
     - **Option 1** : Affichage du message chiffré dans la console
     - **Option 2** : Enregistrement dans un fichier texte (nom personnalisable)


## Caractéristiques techniques
- Gestion automatique des accents et caractères spéciaux
- Support des clés positives et négatives
- Conversion automatique en minuscules pour le traitement
- Conservation des caractères non-alphabétiques (espaces, ponctuation)
- Extension `.txt` systématique pour les fichiers de sortie

## Instructions:
- Clonez le git repository et assurez vous que les fichiers soient dans le bon dossier
- Le dictionnaire doit etre present dans le meme dossier que le repo pour que ca fontionne. 
- Aucun package n'as besoin d'etre instaler.
  
## References:
- SteveKein: Dictionnaire des mots français sous format txt. trié par ordre alphabetique
  Format: TXT
  Nombre de lignes: 336500




