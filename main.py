from enemy import Enemy
from hero import Hero

def main():
    hero_name = input("Entre le nom de votre héros: ")
    
    hero = Hero(hero_name)
    monster_1 = Enemy()
    
    print(hero)
    print(monster_1)
    
    
    
main()