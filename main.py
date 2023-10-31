from character import Character
from enemy import Enemy
from hero import Hero

def main():
    print("")
    print("BIENVUE AU MEILLEUR JEU DU MONDE")
    print("#" * len("BIENVUE AU MEILLEUR JEU DU MONDE"))
    print("")
    hero_name = input("Entre le nom de votre héros: ")
    
    hero = Hero(hero_name)
    monster_1 = Enemy()
    
    print("")
    print("###Infos Héros###")
    print(hero)
    
    print("")
    print("###Infos Ennemi###")
    print(monster_1)
    
    while True:
        print("\nOptions:")
        print("1 - Attaquer ?")
        
        choice = input("Choisissez une option: ")
        
        if choice == "1":
            hero.attack(monster_1)
            
            print("###Infos Ennemi###")
            print(monster_1)
            
        
    
    
    
    
main()