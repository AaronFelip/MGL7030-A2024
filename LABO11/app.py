from flask import Flask, g, jsonify, request
from database import Database
from livre import Livre, insert_schema
from flask_json_schema import JsonValidationError, JsonSchema

app = Flask(__name__)
schema = JsonSchema(app)


def get_db():
    # Créer une ressource si cette dernière n'existe pas
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


# Fermer/ Désaloueer la ressource si elle existe
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()


@app.errorhandler(JsonValidationError)
def validation_error(e):
    errors = [validation_error.message for validation_error in e.errors]
    return jsonify({'error': e.message, 'errors': errors}), 400



@app.route('/api/livre/<int:id>', methods=['GET'])
def get_livre(id):
    livre = get_db().get_livre(id)
    if livre is None:
        return "aucun livre", 404
    else:
        return jsonify(livre.all_info())


@app.route('/api/livre', methods=['POST'])
@schema.validate(insert_schema)
def create_livres():
    data = request.get_json()
    livre = Livre(None, data["titre"], data["auteur"], data["annee"], data["nb_pages"], data["nb_chapitres"])
    livre = get_db().set_livre(livre)
    return jsonify(livre.min_info()), 201























