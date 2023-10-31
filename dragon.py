from enemy import Enemy

class Dragon(Enemy):
    def __init__(self, nom="Dragon", pv=200) -> None:
        super().__init__(nom, pv)
        self.nom = nom
        self.pv = pv