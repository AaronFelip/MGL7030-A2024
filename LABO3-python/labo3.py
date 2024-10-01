# Ce programme permet de construire une facture et de l'écrire sur un fichier

from utils.calculateur_taxes import calculer_taxes
from utils.ecrire_fichier import ouvrir_fichier, fermer_fichier
from utils.fichier import *
# from modules import * // aurait été valide aussi mais peu utile pour la lisibilité


fichier = open("texte_entree")
lignes = fichier.readlines()

# Je force la déclaration de variable dans Python
quantite: int = 0
prix_total: int = 0
items: list[Fichier] = []
numero_produit: int = 0

if __name__ == "__main__":
    for index, line in enumerate(lignes):
        string = line.rstrip("\n").split(" ")
        un_item = Fichier(*string)
        total = (float(un_item.prix) * float(un_item.quantite)) * calculer_taxes(un_item.taxes)
        quantite = quantite + int(un_item.quantite)

        if index == 0:
            output = ouvrir_fichier(un_item.numero_client)

        if index > 0 and un_item.numero_client != items[index - 1].numero_client:
            fermer_fichier(output, prix_total, quantite)
            prix_total = quantite = numero_produit = 0
            output = ouvrir_fichier(un_item.numero_client)

        output.write("%-12s %-14s %4s %8s %10.2f\n" % ("produit #" + str(numero_produit + 1), un_item.numero_produit,
                                                       un_item.quantite, un_item.prix, total))
        prix_total += total
        numero_produit += 1
        items.append(un_item)
    fermer_fichier(output, prix_total, quantite)

