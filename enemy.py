from character import Character

class Enemy(Character):
    def __init__(self, nom, pv) -> None:
        super().__init__(nom, pv)
        
        self.nom = nom
        self.pv = pv
        
    
    def __str__(self):
        return f"- Nom: {self.nom}\n- Point de vie: {self.pv}"
    
    def attack(self, opposant):
        super().attack(opposant)