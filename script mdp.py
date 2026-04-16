import itertools
import string
import time

# Paramètres ajustables
longueur_max = 6  # longueur maximale du mot de passe
jeu_caracteres = string.ascii_lowercase + string.digits  # a-z + 0-9

# Demande du mot de passe à l'utilisateur
mot_de_passe = input("Entre un mot de passe (max 6 caractères, lettres/chiffres) : ")

if len(mot_de_passe) > longueur_max:
    print("Mot de passe trop long !")
    exit()

tentatives = 0
debut = time.time()

trouve = False

# Boucle brute force pédagogique
for longueur in range(1, longueur_max + 1):
    for combinaison in itertools.product(jeu_caracteres, repeat=longueur):
        tentative = ''.join(combinaison)
        tentatives += 1

        if tentative == mot_de_passe:
            fin = time.time()
            print("\nMot de passe trouvé :", tentative)
            print("Nombre de tentatives :", tentatives)
            print("Temps écoulé :", round(fin - debut, 2), "secondes")
            trouve = True
            break
    if trouve:
        break

if not trouve:
    print("Mot de passe non trouvé.")