from character import Character

class Enemy(Character):
    #init de la classe
    def __init__(self, nom, pv, degat = 0) -> None:
        super().__init__(nom, pv)
        
        self.nom = nom
        self.pv = pv
        self.degat = degat
        
    #fonction magique pour listing caractéristique de l'ennemi
    def __str__(self):
        return f"- Nom: {self.nom}\n- Point de vie: {self.pv}"
    
    # on attaque on mode ennemi et on prend le super de la mère qui est commun a ennemie et hero
    def attack(self, opposant):
        super().attack(opposant)
        if opposant.pv <= 0: # test si opposant (heros) est mort
            print(f"\n{opposant.nom} est MORT!!!!!!")
            opposant.continuer()
        
        if self.pv <= 0: # test si on (ennemi) est mort
            print(f"\n{self.nom} est MORT!!!!!!")
            self.full_pv() # on remet des points de vie

