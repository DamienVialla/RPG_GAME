from enemy import Enemy
from const import PV_dragon

class Dragon(Enemy):
    def __init__(self) -> None:
        super().__init__(nom = "Dragon", pv = PV_dragon)
    
    
    def full_pv(self):
        self.pv = PV_dragon