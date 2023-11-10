from character import Character
from dragon import Dragon
from hero import Hero
import pygame
from importer import importer, listing


def main():
    pygame.mixer.init()
    pygame.mixer.music.load("damien.mp3")
    pygame.mixer.music.play()
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
        i=0
        print("\nOptions:")
        print(f"{i} - Importer dossier")
        i+=1
        print(f"{i} - Attaquer ?")
        #on boucle sur l'inventaire du héro pour proposer ce qu'il a dans sa besace
        #l'utilisation d'un objet d'inventaire passe un tour d'attaque
        for item in hero.inventaire: 
            print(f"{hero.inventaire.index(item)+2} - Utiliser {item}") #index+2 car 0 n'existe pas et 1 est forcément attaque
        
        # retransforme le choix en index dans la liste pour aller tester l'objet choisi      
        print()
        choice = int(input("Choisissez une option: "))-2
        
        # attaquer n'étant pas dans la liste et se trouvant tout le temps en choix 1, étant donné qu'on enlève 2, on test la valeur -1
        if choice == -1:
            choice_final = "attaquer"
        elif choice == -2:
            choice_final = "importer"
        else :
            choice_final = hero.inventaire[choice] # le choix final est donc l'objet et pas l'index i qu'on a incrémenté
      
        if choice_final =="importer":
            listing = importer()
            choix = input("Quel nom de personnage souhaitez-vous incarner ?")
            if choix not in listing:
                print("Rentrez un nom valide")
            else :
                hero=Hero(nom = ,inventaire = ,mort = ,degat =, xp = , niveau = ,pv =)
            
        elif choice_final == "attaquer":
            print()
            hero.attack(monster_1)
            monster_1.attack(hero)
        elif choice_final == "potion":
            print()
            hero.potion_soin()
            monster_1.attack(hero)
        elif choice_final == "arme":
            print()
            hero.arme()
            monster_1.attack(hero)
        
        elif choice_final == "armure":
            print()
            hero.armure(monster_1)
            monster_1.attack(hero)
    
            

main()