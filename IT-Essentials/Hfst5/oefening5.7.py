def bepaal_boete(naam, aantal_boeken, aantal_dagen):
    boete = 0
    aanmaningsbrieven = 0

    boete += (aantal_boeken * 0.7) * aantal_dagen
    if aantal_dagen >= 45:
        boete += 0.84
        aanmaningsbrieven = 1

    print(naam + ", je moet €" + str(boete) + " betalen! ")

    return aanmaningsbrieven


def main():
    aantal_aanmaningsbrieven = 0
    naam = input("Geef een naam in: ")

    while naam != "xx":
        aantal_boeken = int(input("Geef het aantal boeken in: "))
        aantal_dagen_overschreden = int(input("Aantal dagen overschreden: "))
        aantal_aanmaningsbrieven += bepaal_boete(naam, aantal_boeken, aantal_dagen_overschreden)
        print("Aantal aanmaningsbrieven: " + str(aantal_aanmaningsbrieven))
        naam = input("Geef een naam in: ")


if __name__ == '__main__':
    main()
