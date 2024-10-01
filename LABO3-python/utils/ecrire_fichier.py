def ouvrir_fichier(numero_client):
    output = open(numero_client + ".txt", "w")
    output.write("Client numéro %s\n\n" % numero_client)
    output.write("%-12s %-14s %4s %8s %10s\n" % (" ", "No de produit", "Qte", "Prix", "Total (tx)"))
    return output


def fermer_fichier(fichier, prix_total, quantite):
    rabais = (prix_total * 0.15) if quantite > 100 else 0
    fichier.write("\nTotal avant rabais: %.2f\n" % prix_total)
    fichier.write("Rabais: %.2f\n" % rabais)
    fichier.write("Total: %.2f\n" % (prix_total - rabais))
    fichier.close()