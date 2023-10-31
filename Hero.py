from character import Character
import random
import sys
class Hero(Character):
    def __init__(self, nom, degat =0, xp =0, niveau =1, pv = 100, ) -> None:
        super().__init__(nom, pv)
        
        self.nom = nom
        self.pv = pv
        self.degat = degat
        self.xp = xp
        self.niveau = niveau
        
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
                self.upgrade()
    
    def upgrade(self):
        self.degat +=5
        self.xp +=25
        if self.xp ==50:
            self.niveau +=1
        print(self)
                    
    def attack(self, opposant):
        super().attack(opposant)
        if opposant.pv <= 0:
            print(f"\n{opposant.nom} est MORT!!!!!!")
            self.continuer()
    
    