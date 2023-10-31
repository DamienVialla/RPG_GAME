from character import Character

class Enemy(Character):
    def __init__(self, nom, PV) -> None:
        super().__init__(nom, PV)