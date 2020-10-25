import datetime


def bepaal_prijs_poort(oppervlakte, prijs_motor):

    return int(((oppervlakte * 113.5 + prijs_motor) * 100) + 0.5) / 100


def genereer_offertenummer(naam, totaalprijs):
    now = str(datetime.datetime.now().year)
    prijs = str(totaalprijs).split(".")

    return now + "_" + naam.upper() + "_" + prijs[0][::-1]


def controleer_hoogte(hoogte):
    if hoogte < 2 or hoogte > 6.5:
        return False
    else:
        return hoogte


def controleer_breedte(breedte):
    if breedte < 2 or breedte > 8:
        return False
    else:
        return breedte


def bepaal_oppervlakte(breedte, hoogte):
    return int(((hoogte * breedte) * 100) + 0.5) / 100


def bepaal_gewicht(oppervlakte):
    return oppervlakte * 11


def bepaal_motorprijs(motornaam):

    if motornaam == "A101":
        return 120
    elif motornaam == "A105":
        return 220.5
    else:
        return 250.5


def bepaal_motornaam(gewicht):
    motornaam = ""
    if gewicht <= 150:
        motornaam = "A101"
    elif gewicht <= 300:
        motornaam = "A105"
    else:
        motornaam = "X300"

    return motornaam


def main():
    naam = input("Naam verkoper: ")
    breedte = float(input("Geef de breedte in van de poort: "))
    hoogte = float(input("Geef de hoogte in van de poort: "))

    while type(controleer_hoogte(hoogte)) != float or type(controleer_breedte(breedte)) != float:
        if controleer_breedte(breedte) == False:
            print("Breedte moet tussen 2m en 8m zijn! ")
            breedte = float(input("Geef breedte in: "))

        if(controleer_hoogte(hoogte)) == False:
            print("Hoogte moet tussen 2m en 6.5m zijn!")
            hoogte = float(input("Geef hoogte in: "))

    oppervlakte = bepaal_oppervlakte(breedte, hoogte)

    print(
        genereer_offertenummer(
            naam, bepaal_prijs_poort(
                oppervlakte, bepaal_motorprijs(
                    bepaal_motornaam(
                        bepaal_gewicht(oppervlakte))))))


if __name__ == '__main__':
    main()
