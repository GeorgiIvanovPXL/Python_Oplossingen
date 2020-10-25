def bereken_conditie_getal(afgelegde_afstand):
    conditie_getal = ((afgelegde_afstand * 1000) - 504.9) / 44.73
    return conditie_getal


def main():
    aantal_deelnemers = 0
    aantal_mannen = 0
    aantal_vrouwen = 0
    geslacht = int(input("Geef het geslacht (1 = man, 2 = vrouw) in : "))
    while geslacht == 1 or geslacht == 2:
        afstand_in_km = float(input("Afstand afgelegd in km na 12 minuten lopen: "))
        aantal_deelnemers += 1

        if bereken_conditie_getal(afstand_in_km) < 29 and geslacht == 2:
            aantal_vrouwen += 1
        if bereken_conditie_getal(afstand_in_km) < 36 and geslacht == 1:
            aantal_mannen += 1
        geslacht = int(input("Geef het geslacht (1 = man, 2 = vrouw) in : "))

    print(((aantal_mannen + aantal_vrouwen) / aantal_deelnemers) * 100)


if __name__ == '__main__':
    main()