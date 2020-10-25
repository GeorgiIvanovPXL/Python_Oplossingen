def hotel_kosten(aantal_nachten):
    aantal_derde_nachten = int(aantal_nachten / 3)
    kosten = (aantal_nachten - aantal_derde_nachten) * 140.50
    return kosten


def vliegtuig_kosten(stad):
    kosten = 0
    if stad == "Barcelona":
        kosten = 183
    elif stad == "Rome":
        kosten = 220
    elif stad == "Berlijn":
        kosten = 125
    else:
        kosten = 450

    return kosten


def huurauto_kosten(aantal_dagen):
    kosten = 40 * aantal_dagen
    korting = 0

    if 3 < aantal_dagen < 7:
        korting = 20
    elif aantal_dagen > 7:
        korting = 30
    else:
        korting = 0

    return kosten - korting


def reis_kosten(stad, aantal_dagen):
    auto_kost = huurauto_kosten(aantal_dagen)
    vlieg_kost = vliegtuig_kosten(stad)
    hotel_kost = hotel_kosten(aantal_dagen - 1)
    kosten = auto_kost + vlieg_kost + hotel_kost

    if stad in "BarcelonaRomeBerlijnOslo":
        return kosten
    else:
        return "Fout, enkel geldig voor: Barcelona, Rome, Berlijn, Oslo "


def main():
    stad = input("Geef stad in: ")
    aantal_dagen = int(input("Geef aantal dagen in: "))

    print("Kosten: €" + str(reis_kosten(stad, aantal_dagen)))


if __name__ == '__main__':
    main()
