from character import Character
from dragon import Dragon
from hero import Hero

def main():
    print("")
    print("BIENVUE AU MEILLEUR JEU DU MONDE")
    print("#" * len("BIENVUE AU MEILLEUR JEU DU MONDE"))
    print("")
    hero_name = input("Entre le nom de votre héros: ")
    
    hero = Hero(hero_name) #instanciation hero
    monster_1 = Dragon() #instanciation code
    
    print("")
    print("###Infos Héros###")
    print(hero)
    
    print("")
    print("###Infos Ennemi###")
    print(monster_1)
    
    while True:
        i=1
        print("\nOptions:")
        print(f"{i} - Attaquer ?")
        #on boucle sur l'inventaire du héro pour proposer ce qu'il a dans sa besace
        #l'utilisation d'un objet d'inventaire passe un tour d'attaque
        for item in hero.inventaire: 
            print(f"{hero.inventaire.index(item)+2} - Utiliser {item}") #index+2 car 0 n'existe pas et 1 est forcément attaque
                
        choice = input("Choisissez une option: ")
        
        #rendre dynamique le traitement du choix en fonction de la boucle ci-dessus => A FAIRE
        if choice == "1":
            print()
            hero.attack(monster_1)
            monster_1.attack(hero)
        
        if choice == "2":
            print()
            hero.potion_soin()
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