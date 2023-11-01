from abc import ABC, abstractclassmethod
import random
from const import low_attack, high_attack
class Character(ABC):
    #init de la classe
    def __init__(self, nom : str, pv: int) -> None:
        self.nom = nom
        self.pv = pv
    
    # Methode commune dans cette partie aux enfants
    # amélioration : idem que plus haut sur l'augmentation des pv en fonction du niveau
    def attack(self, opposant):
        random_attack = (random.randint(low_attack, high_attack)) + (self.degat * 1.05)
        opposant.pv -= random_attack
        message =f"{self.nom} attaque et inflige {random_attack} points à {opposant.nom}"
        if opposant.pv >0:
            message += f" ({opposant.pv} points restant)"
        print(message)
            
        
            
