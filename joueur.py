# class joueur


'''
importation de l'objet gobelet
'''
from gobelet import Gobelet


class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.score = 0
        
    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, nom):
        self._nom = nom
    
    #renvoi le nom du joueur
    def get_nom(self):
        return self.nom
    
    #prend en paramètre le gobelet de la partie, lance le gobelet, met à jour le score dujoueur en fonction du résultat du lancé
    def jouer(self, gobelet):
        gobelet.lancer()
        self.score += gobelet.get_valeur()
        
    #renvoi le score du joueur
    def get_score(self):
        return self.score
    
    #affiche en console le score du joueur
    def afficher_score(self):
        print(f"la valeur du gobelet de {self.nom} est : {self.score}")

    

# j1 = Joueur("bob")
# j1.jouer(Gobelet(3))
# j1.afficher_score()
    