from abc import ABC, abstractclassmethod
import random



class Character:
    def __init__(self, nom : str, pv: int) -> None:
        self.nom = nom
        self.pv = pv
    
    
    def attack(self, opposant):
        random_attack = random.randint(10, 20)
        opposant.pv -= random_attack

