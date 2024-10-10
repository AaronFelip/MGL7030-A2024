from database import Database

# On commence par définir une instance de la classe Databse
db = Database()

def lire_db():
    db.get_all_artistes()
    print("Choisissez un artiste en entrant son id :")
    choix = int(input())
    db.get_album_artiste(choix)

def ecrire_db():
    with open("input.txt", "r") as infile:
        for line in infile :
            splitted_line = line.split('|')
            db.insert_album(splitted_line[0], splitted_line[1], splitted_line[2])
        # Par mesure de sécurité toujours fermer les fichiers après traitement
        infile.close()

if __name__ == "__main__":
    ecrire_db()
    lire_db()
    db.disconnect()