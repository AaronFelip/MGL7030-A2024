import secrets
from datetime import timedelta
from functools import wraps
from flask import Flask, render_template, request, session, redirect, url_for, \
    g, make_response
from urllib.parse import quote
app = Flask(__name__, static_url_path='', static_folder='static')


app.config.update(
    SECRET_KEY=secrets.token_hex(16),
    SESSION_COOKIE_NAME='Session_mon_site_web',
    PERMANENT_SESSION_LIFETIME=timedelta(minutes=30),
)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        users = dict(session).get('id', None)
        if users:
            return f(*args, **kwargs)
        else:
            return render_template('index.html'), 200
    return decorated_function


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()


@app.errorhandler(404)
def page_introuvable(error):
    title = "Erreur 404 - Page introuvable"
    return render_template("404.html", title=title), 404


@app.route("/confirmation")
@login_required
def confirmation():
    title = "Confirmation"
    return render_template("confirmation.html", title=title), 200


@app.route("/", methods=['POST', 'GET'])
def index():
    title = "Accueil"
    if request.method == 'GET':
        return render_template("index.html", title=title), 200
    else:
        courriel = request.form['courriel']
        mdp = request.form['mdp']
        utilisateur = get_db().valider_utilisateur(courriel, mdp)

        if utilisateur is not False:

            session['id'] = utilisateur[0]
            session['prenom'] = utilisateur[1]
            session['nom'] = utilisateur[2]
            session['courriel'] = utilisateur[3]
            session_precedente = request.cookies.get('animal_id', 'non-defini')

            if session_precedente != 'non-defini':
                session['animal_id'] = session_precedente
            else:
                animal = get_db().get_animal_informations(session['id'])
                session['animal_id'] = animal.id
            return redirect('/profil/animal'), 301

        else:
            erreur = "Le nom d'utilisateur ou l'adresse courriel est invalide."
            return render_template("index.html", erreur=erreur,
                                   title=title), 400


@app.route('/deconnexion')
def deconnexion():
    title = "Vous êtes à présent déconnecté"
    animal_id = quote(str(session.get("animal_id", "non-defini")))
    resp = make_response(render_template("deconnection.html",
                                         title=title))
    resp.set_cookie('animal_id', animal_id)

    session.pop('id', None)
    session.pop('nom', None)
    session.pop('prenom', None)
    session.pop('courriel', None)
    session.pop('animal_id', None)

    return resp


@app.context_processor
def animal_list():
    context = {}
    if 'id' in session:
        liste_animaux = get_db().get_animaux_informations(session['id'])
        if liste_animaux:
            context['animal_list'] = [
                {'id': animal.id, 'nom':animal.nom, 'avatar_url': animal.get_avatar_url()}
                for animal in liste_animaux if animal.avatar is not None
            ]
    return context
