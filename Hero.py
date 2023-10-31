from character import Character
from dragon import Dragon
import random
import sys
from const import PV_hero

class Hero(Character):

    liste_mort = ["potion","arme","armure","casque"]

    inventaire =["arme"]
    potion_soin = 20
    
    def __init__(self, nom, mort = False, degat =0, xp =0, niveau =1, pv = PV_hero, ) -> None:
        super().__init__(nom, pv)
        
        self.degat = degat
        self.xp = xp
        self.niveau = niveau
        self.mort = mort
        
    def __str__(self):
        return f"- Nom: {self.nom}\n- Point de vie: {self.pv}\n- Degat : {self.degat}\n- xp :{self.xp}\n- Niveau {self.niveau}"
    
    def full_hero_pv(self):
        self.pv = PV_hero
    
    def continuer(self):
        rejoue = input("Souhaitez-vous faire une partie supplémentaire (O/N) ? ")
        if rejoue != "O" and rejoue != "N":
            print(f"{rejoue} n'est pas un caractère autorisé")
        else :
            if rejoue == "N":
                sys.exit()
            else:
                if self.mort :
                    self.upgrade(-1)
                else :
                    self.upgrade(1)
    
    def upgrade(self, perdu):
        self.full_hero_pv()
        if self.degat !=0:
            self.degat +=5*perdu
        if self.xp !=0:
            self.xp +=25*perdu
        if self.xp  % 50 == 0 and self.xp !=0 :
            self.niveau +=1
            self.pv += 20*perdu
        print(self)
                    
    def attack(self, opposant):
        super().attack(opposant)
        if opposant.pv <= 0:
            opposant.full_pv()
            objet = random.choice(self.liste_mort)
            self.inventaire.append(objet)
            print(f"\n{opposant.nom} est MORT et vous offre {objet} !!!!!!")
            print(f"{self.inventaire}")
            self.continuer()
        
        if self.pv <= 0:
            print(f"\n{self.nom} est MORT!!!!!!")
            opposant.full_pv()
            self.mort = True
            self.continuer()
            

        
    