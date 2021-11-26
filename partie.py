# classe partie 
'''
contient la logique du jeu
    - Nombre de dés
    - lance le gobelet
    - création des utilisateurs => nom
    - affiche les scores de chaque joueur une fois le nombre de round atteint
    - afficher les étapes

'''
from joueur import Joueur
from gobelet import Gobelet
import operator

class Partie:
    def __init__(self, nb_tours, nb_des, noms_joueurs):
        self.nb_tours = nb_tours
        self.nb_des = nb_des
        self.joueurs = []
        self.noms_joueurs = noms_joueurs
        self.gobelet = Gobelet(self.nb_des)
        self.initialiser()
        
    
    @property
    def nb_tours(self):
        return self._nb_tours
    
    @nb_tours.setter
    def nb_tours(self, nb_tours):
        self._nb_tours = nb_tours
    
    @property
    def nb_des(self):
        return self._nb_des
    
    @nb_des.setter
    def nb_des(self, nb_des):
        self._nb_des = nb_des
    
    @property
    def joueurs(self):
        return self._joueurs
    
    @joueurs.setter
    def joueurs(self, joueurs):
        self._joueurs = joueurs
    
    @property
    def noms_joueurs(self):
        return self._noms_joueurs
    
    @noms_joueurs.setter
    def noms_joueurs(self, noms_joueurs):
        self._noms_joueurs = noms_joueurs
    
    
    # permet d'inscrire des joueurs dans la partie
    def initialiser(self):
        
        for nom in self.noms_joueurs:
            self.joueurs.append(Joueur(nom))

    
    '''
    lance la partie : chaque joueur joue à tour de rôle pendant les n tours. 
    Une fois la partie terminée, affiche le gagnant.
    '''
    def lancer(self):
            
        for tour in range(self.nb_tours): 
            for joueur in (self.joueurs):
                gobelet = Gobelet(self.nb_des)
                joueur.jouer(gobelet)
                print(f"{joueur.get_nom()} a joué {gobelet.get_valeur()}")
                print(joueur.get_nom(), "obtient un score de : ", joueur.get_score())

      
    # compare les scores des joueurs et affiche le gagnant.
    '''
    création d'un dictionnaire avec le nom des joueurs en clé et leur score en valeur
    je cherche ensuite la valeur max
    '''
    def afficher_gagnant(self):
        score_final = {}
        for joueur in self.joueurs:
            print("\n", "*****", joueur.get_nom(), "obtient un score total de : ", joueur.get_score(), "*****", "\n")
            score_final[joueur.get_nom()] = joueur.get_score()
        
        #pour vérifier que le dictionnaire fonctionne  
        # for cle, valeur in score_final.items():
        #     print(cle(), valeur())     

        # pour extraire le gagnant ayant la valeur max dans le dictionnaire
        max_key = max(score_final.items(), key=operator.itemgetter(1))[0]
        print("le gagant est : ", max_key, "\n")  

        listOfKeys = list()
        #test pour le cas ou il y aurait plusieurs scores identiques
        for key, value in score_final.items():
            if value == max_key[0]:
                listOfKeys.append(key)
                print('les joueurs ayant les scores les plus élevés sont : ', listOfKeys)



# pour vérifier que cela fonctionne !
#==================================================  
# p = Partie(5, 2, ["Francois", "Tommy"])
# p.lancer()
# p.afficher_gagnant()

