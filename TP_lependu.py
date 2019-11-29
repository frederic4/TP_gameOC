# jeu de pendu qui prend un mot au hasard dans une liste (fichier le_pendu_liste)
# Créer un fichier avec la liste des mots
# créer un fichier avec la fonction qui récupère le mot et la fonction.


from random import*
from le_pendu_liste import *
from les_fonctions_pendu import *


mot_a_trouver = choisir_mot()
lettres_trouvees = []
mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)
nb_chances =7
while mot_a_trouver!=mot_trouve and nb_chances>0:
    print("Mot à trouver {0} (encore {1} chances)".format(mot_trouve, nb_chances))
    lettre = recup_lettre()
    if lettre in lettres_trouvees: # La lettre a déjà été choisie
        print("Vous avez déjà choisi cette lettre.")
    elif lettre in mot_a_trouver: # La lettre est dans le mot à trouver
        lettres_trouvees.append(lettre)
        print("Bien joué.")
    else:
        nb_chances -= 1
        print("... non, cette lettre ne se trouve pas dans le mot...")
    mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)

# A-t-on trouvé le mot ou nos chances sont épuisées ?
if mot_a_trouver==mot_trouve:
    print("Félicitations ! Vous avez trouvé le mot {0}.".format(mot_a_trouver))
else:
    print("PENDU !!! Vous avez perdu.")
continuer_partie = input("Souhaitez-vous continuer la partie (y/n) ? ")
if continuer_partie=='y':
    