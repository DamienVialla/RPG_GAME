from enemy import Enemy

class Wolf(Enemy):
    def __init__(self, nom="Wolf", pv=80) -> None:
        super().__init__(nom, pv)
        self.nom = nom
        self.pv = pv