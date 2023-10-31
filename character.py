from abc import ABC, abstractclassmethod
import random
import sys



class Character:
    def __init__(self, nom : str, pv: int) -> None:
        self.nom = nom
        self.pv = pv
    
    
    def attack(self, opposant):
        random_attack = random.randint(10, 20)
        opposant.pv -= random_attack
        print(f"Vous avez enlevé {random_attack} points à {opposant.nom} ")
        if opposant.pv <= 0:
            print(f"{opposant.nom} est MORT!!!!!!")
            sys.exit()
