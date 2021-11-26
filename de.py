# class dé => création du dé à 6 face
'''

methodes
    - get_valeur() : renvoie la valeur du dé
    -lancer() : change la valeur du dé ->cette valeur doit être un nombre généré aléatoirement entre 1 et 6


'''

import random

class De:
    def __init__(self):
        self.valeur = 0
    
    #méthodes
    
    def lancer(self):
        self.valeur = int(random.randint(1, 6))
        #print(self.valeur) #pour tester
    
    def get_valeur(self):
        #print(f"le résutat du lancé est : {self.valeur}")
        return self.valeur

#pour tester
'''
lancer1 = De()
print(lancer1)

'''      


