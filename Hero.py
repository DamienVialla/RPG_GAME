from character import Character

class Hero(Character):
    def __init__(self, nom, PV) -> None:
        super().__init__(nom, PV)