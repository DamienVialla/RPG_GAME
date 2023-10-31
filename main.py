from character import Character
from dragon import Dragon
from hero import Hero

def main():
    print("")
    print("BIENVUE AU MEILLEUR JEU DU MONDE")
    print("#" * len("BIENVUE AU MEILLEUR JEU DU MONDE"))
    print("")
    hero_name = input("Entre le nom de votre héros: ")
    
    hero = Hero(hero_name)
    monster_1 = Dragon()
    
    print("")
    print("###Infos Héros###")
    print(hero)
    
    print("")
    print("###Infos Ennemi###")
    print(monster_1)
    
    while True:
        i=1
        print("\nOptions:")
        print("1 - Attaquer ?")
        if "potion" in hero.inventaire:
            print("2 - Utiliser potion soin ?")
                
        if "arme" in hero.inventaire:
            print("3 - Utiliser arme ?")
            
        if "armure" in hero.inventaire:
            print("4 - Utiliser armure ?")
        
        if "casque" in hero.inventaire:
            print("5 - Utiliser casque ?")
            
                
        choice = input("Choisissez une option: ")
        
        if choice == "1":
            print()
            hero.attack(monster_1)
            monster_1.attack(hero)
        
        if choice == "2":
            print()
            #méthode pour vider inventaire de potion et augmenter les pv
            monster_1.attack(hero)
        
        if choice == "3":
            print()
            #méthode pour vider inventaire de arme et augmenter les degat
            monster_1.attack(hero)
        
        if choice == "4":
            print()
            #méthode pour vider inventaire de armure et diminue attaque
            monster_1.attack(hero)
        
        if choice == "5":
            print()
            #méthode pour vider inventaire de casque et diminue attaque
            monster_1.attack(hero)
            
            

    

    
main()