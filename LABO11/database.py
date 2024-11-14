import sqlite3
from livre import Livre

class Database:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/db.db')
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    def get_livres(self):
        cursor = self.get_connection().cursor()
        cursor.execute('SELECT * FROM livre')
        livres = cursor.fetchall()
        return (Livre(livre[0], livre[1],livre[2], livre[3], livre[4], livre[5]) for livre in livres)


    def get_livre(self, id):
        cursor = self.get_connection().cursor()
        cursor.execute('SELECT * FROM livre WHERE id=?', (id,))
        livre = cursor.fetchone()
        if livre is None:
            return None
        else:
            return(Livre(livre[0], livre[1], livre[2], livre[3], livre[4], livre[5]))

    def set_livre(self, livre):
        connection = self.get_connection()
        connection.execute(
            'INSERT INTO livre(titre, auteur, annee, nb_pages, nb_chapitres)' 'VALUES (?, ?, ?, ?, ?)',
            (livre.titre, livre.auteur, livre.annee, livre.nb_pages, livre.nb_chapitres))
        connection.commit()
        cursor = connection.cursor()
        cursor.execute('SELECT last_insert_rowid()')
        result = cursor.fetchone()
        livre.set_id(result[0])
        return livre

    def delete_livre(self, id):
        connection = self.get_connection()
        connection.execute("DELETE FROM livre WHERE id=?", (id,))
        connection.commit()















