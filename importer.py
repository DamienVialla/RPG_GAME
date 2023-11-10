import json

def importer():
    try:
        with open("./donnees.json", "r") as fichier:
            listing = json.load(fichier)
    except FileNotFoundError:
        listing = []
    
    return listing
    #for personnage in listing :
    #    print(f"nom : {personnage['nom']} - Inventaire : {personnage['inventaire']} - mort : {personnage['mort']} - dégat : {personnage['degat']} - xp : {personnage['xp']} - niveau : {personnage['niveau']} - pv : {personnage['pv']}")
    
    