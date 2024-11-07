from flask import Flask, render_template, request, url_for, redirect
import re
app = Flask(__name__, static_url_path='', static_folder='static')


# Fonctions de validation externes
def champs_remplis(nom, prenom, date, genre, code):
    return all([nom, prenom, date, genre, code])


def valider_date(date):
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    return bool(re.match(pattern, date))


def valider_genre(genre):
    return genre.upper() in ["M", "F"]


def valider_code(code, nom, prenom, date, genre):

    format_general = r"^[A-Z]{4}\d{8}$"
    if not re.match(format_general, code):
        return False

    if code[:3] != nom[:3].upper() or code[3] != prenom[0].upper():
        return False

    jour = date[8:]
    if code[4:6] != jour:
        return False

    mois = int(date[5:7])
    mois_code = int(code[6:8])
    if (genre.upper() == "F" and mois_code != mois + 50) or (
            genre.upper() == "M" and mois_code != mois):
        return False

    annee = date[2:4]
    if code[8:10] != annee:
        return False

    return True


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        # Récupération des valeurs du formulaire
        form_data = {
            "nom": request.form["nom"],
            "prenom": request.form['prenom'],
            "date": request.form['date'],
            "genre": request.form['genre'],
            "code": request.form['code']
        }

        # Exécution des validations et vérification des erreurs
        validations = [
            champs_remplis(form_data["nom"], form_data["prenom"],
                           form_data["date"], form_data["genre"],
                           form_data["code"]),
            valider_date(form_data["date"]),
            valider_genre(form_data["genre"]),
            valider_code(form_data["code"], form_data["nom"],
                         form_data["prenom"], form_data["date"],
                         form_data["genre"])
        ]

        # Si une validation échoue, recharger la page avec les données
        if not all(validations):
            return render_template('index.html', **form_data)

        # Si toutes les validations passent, rediriger vers la page de confirmation
        return redirect(url_for('confirmation'))

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')


















