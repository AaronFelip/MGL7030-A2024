class Livre:
    def __init__(self, id, titre, auteur, annee, nb_pages, nb_chapitres):
        self.id = id
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.nb_pages = nb_pages
        self.nb_chapitres = nb_chapitres

    def set_id(self, id):
        self.id = id

    def min_info(self):
        return {
            'id': self.id,
            'titre': self.titre,
        }

    def all_info(self):
        return {
            'id': self.id,
            'titre': self.titre,
            'auteur': self.auteur,
            'annee': self.annee,
            'nb_pages': self.nb_pages,
            'nb_chapitres': self.nb_chapitres
        }


insert_schema = {
    'type' : 'object',
    'required' : ['titre', 'auteur', 'annee', 'nb_pages', 'nb_chapitres'],
    'properties' : {
        'titre' : {
            'type' : 'string'
        },
        'auteur' : {
            'type' : 'string'
        },
        'annee' : {
            'type' : 'number'
        },
        'nb_pages' : {
            'type' : 'number'
        },
        'nb_chapitres' : {
            'type' : 'number'
        }
    },
    'additionalProperties': False
}