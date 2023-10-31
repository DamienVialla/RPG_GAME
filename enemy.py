from character import Character

class Enemy(Character):
    def __init__(self, nom, pv, degat = 0) -> None:
        super().__init__(nom, pv)
        
        self.nom = nom
        self.pv = pv
        self.degat = degat
        
    
    def __str__(self):
        return f"- Nom: {self.nom}\n- Point de vie: {self.pv}"
    
    def attack(self, opposant):
        super().attack(opposant)
        if opposant.pv <= 0:
            print(f"\n{opposant.nom} est MORT!!!!!!")
            opposant.continuer()
        
        if self.pv <= 0:
            print(f"\n{self.nom} est MORT!!!!!!")
            self.full_pv()

