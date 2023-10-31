from abc import ABC, abstractclassmethod
import random

class Character(ABC):
    def __init__(self, nom : str, pv: int) -> None:
        self.nom = nom
        self.pv = pv
    
    
    def attack(self, opposant):
        low_attack = 10 
        high_attack = 20
        random_attack = (random.randint(low_attack, high_attack)) + (self.degat * 1.05)
        opposant.pv -= random_attack
        message =f"{self.nom} attaque et inflige {random_attack} points à {opposant.nom}"
        if opposant.pv >0:
            message += f" ({opposant.pv} points restant)"
        print(message)
            
        
            
