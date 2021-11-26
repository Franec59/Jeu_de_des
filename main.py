from de import De
from gobelet import Gobelet
from joueur import Joueur
from partie import Partie



print("jeu de dés")
print("commencer la partie")
tour = input("Entrer le nombre de tour de jeu : ")
tour = int(tour)
nbre_des = input("Entrer le nombre de dés : ")
nbre_des = int(nbre_des)
nbre_de_joueur = input("Entrer le nombre de joueur : ")
nbre_de_joueur = int(nbre_de_joueur)

liste_joueur = []
def nomDesJoueurs():
    for j in range(nbre_de_joueur):
        nom = input(f"entrer le nom du joueur {j+1} : ")
        liste_joueur.append(nom)

nomDesJoueurs()
p = Partie(tour, nbre_des, liste_joueur)
p.lancer()
p.afficher_gagnant()

