import sqlite3

class Database():

    # Definir le constructeur de la classe
    def __init__(self):
        self.connection = None

    # Definir une connexion avec la base de données
    # Dans notre cas c'est la base de données créée à partir du script sql donné
    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db/musique.db")
        return self.connection

    # Deconnexion de la base de données
    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def get_all_artistes(self):
        # On commence par defenir un curseur pour etablir la connextion
        # avec la base de données et effectuer les requettes necessaires
        cursor = self.get_connection().cursor()
        # On execute la requete de recherche
        cursor.execute("SELECT * FROM artiste")
        # On range toutes les données dans des variables
        for row in cursor:
            identifier, nom, est_solo, combien = row
            # On affiche le résultat à la console
            print("Artiste n: %d Nom : %s\n" %(identifier, nom))

    def get_album_artiste(self, id):
        cursor = self.get_connection().cursor()
        # WHERE permet de selectionner l'album de l'artiste avec l'id donné
        cursor.execute("SELECT titre, annee FROM album WHERE artiste_id=%d" %id)
        for row in cursor:
            # On range le titre et l'année récupérés dans des variables
            titre, annee = row
            # On affiche le résultat à la console
            print("%s %d\n" %(titre, annee))

    def insert_album(self, nom_artiste, nom_album, annee):
        # On sépare la connexion et le curseur
        # La connexion servira a committer les changements dans la base de données
        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT id FROM artiste WHERE nom LIKE ?", ('%'+nom_artiste+'%',))
        # On fetch les id des artistes qui matchent (si ils existent)
        existe = cursor.fetchall()
        #print(existe)

        if existe:
            # On récupere l'id
            # Decommentez la trace (les prints) pour une explication un peu plus "visuelle" :)
            id_artiste = existe[0][0]
            #print(id_artiste)
            # On update les donnees de l'artiste correspondant a artiste_id en ajoutant le nouvel album à la table album
            cursor.execute(("INSERT INTO album (titre, annee, artiste_id)" "VALUES(?,?,?)"), (nom_album, annee, id_artiste))
            # On commmit les changements
            connection.commit()
        else:
            # On insère le nouvel artiste dans la table artiste
            cursor.execute(("INSERT INTO artiste (nom, est_solo, nombre_individus)" "VALUES(?, ?, ?)"), (nom_artiste, 0, 1))
            # On récupere l'id du dernier artiste ajouté
            cursor.execute("SELECT last_insert_rowid()")
            last_id = cursor.fetchone()[0]
            connection.commit()
            # A partir de l'id du dernier artiste ajouté on ajoute son album a la table album
            cursor.execute(("INSERT INTO album (titre, annee, artiste_id)" "VALUES(?, ?, ?)"), (nom_album, annee, last_id))
            connection.commit()
