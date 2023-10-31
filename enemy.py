from character import Character

class Enemy(Character):
    def __init__(self, nom, pv = 80) -> None:
        super().__init__(nom, pv)
        
        self.pv = pv
        self.nom = nom
    
    def __str__(self):
        return f"- Nom: {self.nom}\n- Point de vie: {self.pv}"