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


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
