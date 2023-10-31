from character import Character
from dragon import Dragon
import random
import sys
class Hero(Character):
    def __init__(self, nom, mort = False, degat =0, xp =0, niveau =1, pv = 30, ) -> None:
        super().__init__(nom, pv)
        
        self.degat = degat
        self.xp = xp
        self.niveau = niveau
        self.mort = mort
        
    def __str__(self):
        return f"- Nom: {self.nom}\n- Point de vie: {self.pv}\n- Degat : {self.degat}\n- xp :{self.xp}\n- Niveau {self.niveau}"
    
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
    
    def upgrade(self,perdu:int):
        self.degat +=5*perdu
        self.xp +=25*perdu
        if self.xp  % 50 == 0:
            self.niveau +=1
            self.pv += 20*perdu
        print(self)
                    
    def attack(self, opposant):
        super().attack(opposant)
        if opposant.pv <= 0:
            print(f"\n{opposant.nom} est MORT!!!!!!")
            opposant.full_pv()
            self.continuer()
        elif self.pv <= 0:
            print(f"\n{self.nom} est MORT!!!!!!")
            opposant.full_pv()
            self.mort = True
            self.continuer()
            

        
    