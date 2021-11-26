# class gobelet
'''
Deux attributs :
    -Valeur: nombre représentant la valeur d'un lancer du gobelet
    -Des: tableau de dés qui contient un certain nombre de dés
    
Un constructeur 
    -Avec un argument constructor(nb_des) : 
        initialise la valeur du gobelet à 0, génère le nombre de dés nécessaires à la partie et les ajoute au tableau des

Ainsi que 3 méthodes :
    -get_valeur() : renvoie la valeur du gobelet
    -lancer() : change la valeur des dés du gobelet ; met à jour la valeur du gobelet
    -afficher_score() :affiche en console le score du dernier lancé de gobelet
    
'''

from de import De

class Gobelet:
    def __init__(self, nb_des):
        self.nb_des = nb_des
        self.des = []
        self.valeur = 0
    
        
    @property
    def nb_des(self):
        return self._nb_des
    
    @nb_des.setter
    def nb_des(self, nb_des):
        self._nb_des = nb_des
    
    #méthode pour lancer un nombre de dés depuis De
    def lancer(self):
        for i in range(self.nb_des):
            monDe = De()
            monDe.lancer()
            self.des.append(monDe)
            #pour avoir la valeur total du gobelet ( somme des dés )
            self.valeur += monDe.get_valeur()
    
    #méthode pour recupérer la valeur du gobelet
    def get_valeur(self):
        return self.valeur
    
    def afficher_score(self):
        print(f"la valeur du gobelet est : {self.valeur}")


#pour tester
# gobelet = Gobelet(3)
# gobelet.lancer()
# gobelet.afficher_score()

# print(gobelet.get_valeur())
    