from enemy import Enemy

class Dragon(Enemy):
    def __init__(self) -> None:
        super().__init__(nom = "Dragon", pv = 50)
    
    
    def full_pv(self):
        self.pv = 50