from character import Character
from enemy import Enemy
from hero import Hero

def main():
    hero_name = input("Entre le nom de votre héros: ")
    
    hero = Hero(hero_name)
    monster_1 = Enemy()
    
    print("######")
    print(hero)
    print(monster_1)
    print("######")
    
    hero.attack(monster_1)
    
    print(monster_1)
    
    monster_1.attack(hero)
    
    print(hero)
    
    
    
main()