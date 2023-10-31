from abc import ABC, abstractclassmethod
import random

class Character(ABC):
    def __init__(self, nom : str, pv: int) -> None:
        self.nom = nom
        self.pv = pv
    
    
    def attack(self, opposant):
        random_attack = random.randint(10, 20)
        opposant.pv -= random_attack
        message =f"{self.nom} attaque et inflige {random_attack} points à {opposant.nom}"
        if opposant.pv >0:
            message += f" ({opposant.pv} points restant)"
        print(message)
            
        
            
