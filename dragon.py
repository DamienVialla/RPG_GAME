from enemy import Enemy
from const import PV_dragon

class Dragon(Enemy):
    #init de la classe
    def __init__(self) -> None:
        super().__init__(nom = "Dragon", pv = PV_dragon)
    
    #redonne tous les points de vie de héros (attention ne pourrait pas être appelé différemment en reprenant le init ?)
    def full_pv(self):
        self.pv = PV_dragon