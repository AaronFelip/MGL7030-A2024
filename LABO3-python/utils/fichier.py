# Classe permettant la création d'un objet de type fichier

class Fichier(object):
    def __init__(self, numero_client: str, numero_produit: str, quantite: str, prix: str, taxes: str = None):
        self.numero_client = numero_client
        self.numero_produit = numero_produit
        self.quantite = quantite
        self.prix = prix
        self.taxes = taxes