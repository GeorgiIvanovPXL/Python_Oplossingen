def bereken_lidgeld(leeftijd, aantal_kinderen, inkomen, aansluitingsjaar):

    lidgeld = 100

    if leeftijd > 60:
        lidgeld -= 15

    if aantal_kinderen > 0:
        if aantal_kinderen * 7.5 > 35:
            lidgeld -= 35
        else:
            lidgeld -= aantal_kinderen * 7.5

    if 2020 - aansluitingsjaar > 20:
        lidgeld -= 12.5

    if inkomen < 7500:
        lidgeld -= 25

    if lidgeld < 50:
        lidgeld = 50

    return lidgeld


def main():
    naam = input("Geef je naam in: ")
    while not(naam == "X" or naam == "x"):
        leeftijd = int(input("Geef je leeftijd in: "))
        aantal_kinderen_ten_laste = int(input("Aantal kinderen ten laste: "))
        inkomen = int(input("Inkomen: "))
        aansluitingsjaar = int(input("Aansluitingsjaar: "))
        print(naam + " moet € " + str((leeftijd, aantal_kinderen_ten_laste, inkomen, aansluitingsjaar)) + " betalen! ")
        naam = input("Geef je naam in: ")


if __name__ == '__main__':
    main()
