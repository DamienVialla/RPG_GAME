from character import Character
from dragon import Dragon
import random
import sys
from const import *

class Hero(Character):

    liste_mort = ["potion","arme","armure"] #liste des objets que peut donner un monstre quand il meurt
    
    #init de la classe
    def __init__(self, nom, inventaire = [], mort = False, degat =0, xp =0, niveau =1, pv = PV_hero, ) -> None:
        super().__init__(nom, pv)
        
        self.degat = degat
        self.xp = xp
        self.niveau = niveau
        self.mort = mort
        self.inventaire = inventaire
    
    #fonction magique pour listing caractéristique du héros    
    def __str__(self):
        return f"- Nom: {self.nom}\n- Point de vie: {self.pv}\n- Degat : {self.degat}\n- xp :{self.xp}\n- Niveau {self.niveau}"
    
    #redonne tous les points de vie de héros (attention ne pourrait pas être appelé différemment en reprenant le init ?)
    def full_hero_pv(self):
        self.pv = PV_hero
    
    #fin de partie, on propose au joueur d'en refaire une
    def continuer(self):
        print()
        rejoue = input("Souhaitez-vous faire une partie supplémentaire (O/N) ? ")
        if rejoue != "O" and rejoue != "N":
            print(f"{rejoue} n'est pas un caractère autorisé")
        else :
            if rejoue == "N":
                sys.exit() #sortie du système
            else:
                if self.mort : #test si c'est le joueur qui est mort ou l'ennemi et en fonction on change attribut pour upgrade plus bas
                    self.upgrade(-1)
                else :
                    self.upgrade(1)
    
    # amélioration héros (ou pas) à la fin de la partie => appelé par continuer()
    # possible amélioration : rendre les valeurs interactive en fonction du niveau
    # possible amélioration : mettre dans le fichier const ces valeurs qui sont en dur
    def upgrade(self, perdu):
        self.full_hero_pv()
        if self.degat !=0: #test si déjà à zéro
            self.degat +=augmentation_degat*perdu
        if self.xp !=0:
            self.xp +=augmentation_xp*perdu
        if self.xp  % 50 == 0 and self.xp !=0 :# test si modulo 50 (limite pour passer niveau) et si ce n'est pas zéro
            self.niveau +=1
            self.pv += augmentation_pv*perdu
        print(self)
    
    # on attaque en mode hero et on prend le super de la mère qui est commun a ennemie et hero                
    def attack(self, opposant):
        super().attack(opposant)
        if opposant.pv <= 0: # test si opposant est mort
            opposant.full_pv() # remet les points de vie
            objet = random.choice(self.liste_mort) # objet prend une objet aléatoire dans la liste
            phrase_ajout_objet = f"\n{opposant.nom} est MORT et il vous offre {objet} !!!"
            if objet in self.inventaire : # test si objet déjà dans inventaire
                phrase_ajout_objet += f" Vous en avez déjà {objet} dans votre inventaire, {objet} ne peut pas être ajouté"
                print(phrase_ajout_objet)
            else :
                self.inventaire.append(objet) # on ajoute cet objet à l'inventaire.
                print(phrase_ajout_objet)
            
            print()
            print(f"Voici votre inventaire actuel : {self.inventaire}")
            self.continuer()
        
        if self.pv <= 0: # test si on est mort
            print(f"\n{self.nom} est MORT!!!!!!")
            opposant.full_pv() # remet les points de vie
            self.mort = True # on change le statue de notre hero pour upgrade
            self.continuer()
    
    # si choix potion de vie plutot que d'attaquer
    # amélioration : idem que plus haut sur l'augmentation des pv en fonction du niveau
    def potion_soin(self):
        self.inventaire.remove("potion") # on enlève la potion dans l'inventaire
        mess_potion = f"{self.nom}, vous êtes passé de {self.pv} pv à "
        self.pv += random.randint(low_soin,high_soin) # on randomise l'augmentation des points de vie. Attention il faudrait défaquer cette augmentation au prochain niveau sinon c'est exponentiel le truc
        mess_potion += f"{self.pv} pv." 
        print(mess_potion) # on informe
    
    # si choix arme plutot que d'attaquer
    # amélioration : idem que plus haut sur l'augmentation des pv en fonction du niveau
    def arme(self):
        self.inventaire.remove("arme") # on enlève arme dans l'inventaire
        mess_degat = f"{self.nom}, vous êtes passé de {self.degat} dégat à " 
        self.degat += random.randint(low_arme,high_arme) # on randomise l'augmentation des dégats. Attention il faudrait défaquer cette augmentation au prochain niveau sinon c'est exponentiel le truc
        mess_degat += f"{self.degat} points."
        print(mess_degat) # on informe
    
    # si choix armure plutot que d'attaquer
    # amélioration : idem que plus haut sur l'augmentation des pv en fonction du niveau
    def armure(self,opposant):
        self.inventaire.remove("armure") # on enlève arme dans l'inventaire
        mess_armure = f"{opposant.nom} a ses attaques diminuées de " 
        opposant.degat -= random.randint(low_degat,high_degat) # on randomise la diminution des dégats de l'opposant. Attention il faudrait défaquer cette augmentation au prochain niveau sinon c'est exponentiel le truc
        mess_degat += f"{opposant.degat} points."
        print(mess_degat) # on informe
         

        
    