import sqlite3


class Database():

    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/db.db')
        return self.connection

    def deconnection(self):
        if self.connection is not None:
            self.connection.close()

    def get_all_artistes(self):
        try:
            # On commence par définir un curseur pour établir la connexion
            # avec la base de données et effectuer les requêtes nécessaires
            cursor = self.get_connection().cursor()
            # On exécute la requête pour récupérer tous les artistes
            cursor.execute("SELECT * FROM artiste")

            artistes = []

            # On récupère les résultats et on les stocke dans une liste tout en les affichant à la console
            for row in cursor:
                identifier, nom, est_solo, combien = row
                # Affiche l'identifiant et le nom de l'artiste dans la console
                print("Artiste n°: %d Nom : %s\n" % (identifier, nom))
                # Ajoute les informations de l'artiste dans la liste
                artistes.append(
                    {'id': identifier, 'name': nom, 'is_solo': est_solo,
                     'number_of_albums': combien})

            return artistes  # On retourne la liste des artistes

        except Exception as e:
            print(f"Erreur lors de la récupération des artistes : {str(e)}")
            return []  # En cas d'erreur, on retourne une liste vide


    def get_album_artiste(self, id):
        try:
            cursor = self.get_connection().cursor()
            # WHERE permet de sélectionner l'album de l'artiste avec l'id donné
            cursor.execute(
                "SELECT titre, annee FROM album WHERE artiste_id=%d" % id)

            albums = []

            # On récupère les résultats et on les stocke dans une liste tout en les affichant à la console
            for row in cursor:
                titre, annee = row
                # Affiche le titre et l'année dans la console
                print("%s %d\n" % (titre, annee))
                # Ajoute le titre et l'année dans la liste d'albums à retourner
                albums.append({'titre': titre, 'annee': annee})

            return albums  # On retourne la liste des albums

        except Exception as e:
            print(
                f"Erreur lors de la récupération des albums pour l'artiste {id}: {str(e)}")
            return []  # En cas d'erreur, on retourne une liste vide

    def insert_album(self, nom_artiste, nom_album, annee):
        # On sépare la connexion et le curseur
        # La connexion servira a committer les changements dans la base de données
        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT id FROM artiste WHERE nom LIKE ?",
                       ('%' + nom_artiste + '%',))
        # On fetch les id des artistes qui matchent (si ils existent)
        existe = cursor.fetchall()
        # print(existe)

        if existe:
            # On récupere l'id
            # Decommentez la trace (les prints) pour une explication un peu plus "visuelle" :)
            id_artiste = existe[0][0]
            # print(id_artiste)
            # On update les donnees de l'artiste correspondant a artiste_id en ajoutant le nouvel album à la table album
            cursor.execute((
                               "INSERT INTO album (titre, annee, artiste_id)" "VALUES(?,?,?)"),
                           (nom_album, annee, id_artiste))
            # On commmit les changements
            connection.commit()
        else:
            # On insère le nouvel artiste dans la table artiste
            cursor.execute((
                               "INSERT INTO artiste (nom, est_solo, nombre_individus)" "VALUES(?, ?, ?)"),
                           (nom_artiste, 0, 1))
            # On récupere l'id du dernier artiste ajouté
            cursor.execute("SELECT last_insert_rowid()")
            last_id = cursor.fetchone()[0]
            connection.commit()
            # A partir de l'id du dernier artiste ajouté on ajoute son album a la table album
            cursor.execute((
                               "INSERT INTO album (titre, annee, artiste_id)" "VALUES(?, ?, ?)"),
                           (nom_album, annee, last_id))
            connection.commit()


    def get_artiste(self, id):
        cursor = self.get_connection().cursor()
        cursor.execute("SELECT nom FROM artiste WHERE id=?", (id,))
        artiste = cursor.fetchone()  # On récupère le nom de l'artiste
        return artiste[0] if artiste else "Artiste inconnu"
