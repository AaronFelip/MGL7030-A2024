def calculer_taxes(type_taxes):
    taxes = 0
    if type_taxes == "FP":
        taxes = 1.14975
    elif type_taxes == "F":
        taxes = 1.05
    elif type_taxes == "P":
        taxes = 1.09975
    else:
        taxes = 1
    return taxes