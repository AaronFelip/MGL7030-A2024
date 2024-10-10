from flask import Flask, render_template, request, redirect, url_for, g
from database import Database

app = Flask(__name__, static_folder='static')


def get_db():
    # Récupère la base de données associée à la requête actuelle, si elle existe déjà dans `g`
    database = getattr(g, "_database", None)

    # Si aucune connexion n'existe, on en crée une nouvelle et on l'associe à `g._database`
    if database is None:
        g._database = Database()

    # Retourne la connexion à la base de données pour l'utiliser dans d'autres fonctions
    return g._database


# Fonction pour fermer la connexion à la base de données à la fin de la requête
@app.teardown_appcontext
def deconnection(exception):
    # Récupère la connexion de la base de données associée à `g`
    database = getattr(g, "_database", None)
    if database is not None:
        database.deconnection()


@app.route('/')
def index():
    artistes = get_db().get_all_artistes()
    return render_template('index.html', artistes=artistes)


@app.route('/artiste/<int:artiste_id>')
def albums_par_artiste(artiste_id):
    # On récupère les albums de l'artiste sélectionné
    albums = get_db().get_album_artiste(artiste_id)

    # Récupère le nom de l'artiste pour l'afficher sur la page
    artiste = get_db().get_artiste(artiste_id)

    # On retourne un template distinct pour afficher les albums
    return render_template('album.html', albums=albums, artiste=artiste)


# Route pour insérer des albums à partir du fichier `input.txt`
@app.route('/insert_albums')
def insert_albums():
    try:
        # Ouvre le fichier `input.txt` en mode lecture et écriture
        with open("input.txt", "r+") as infile:
            # Parcourt chaque ligne du fichier
            for line in infile:
                # Divise chaque ligne par le caractère `|` pour extraire les champs de l'album
                splitted_line = line.split('|')

                # Insère l'album dans la base de données
                get_db().insert_album(splitted_line[0], splitted_line[1],
                                      splitted_line[2])

            # Ferme le fichier après lecture
            infile.close()

        # Redirige vers la page principale après insertion pour actualiser la liste
        return redirect(url_for('index'))
    except Exception as e:
        # En cas d'erreur, retourne un message d'erreur
        return str(e)


