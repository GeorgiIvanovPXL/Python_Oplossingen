import math


def bereken_kostprijs(oppervlakte):
    aantal_uur = math.ceil(oppervlakte / 160)
    return int(((aantal_uur * 12.5) * 100)+0.5) / 100


def bereken_aantal_werkers_en_aantal_uur(oppervlakte):

    aantal_personen = math.floor(oppervlakte / 1280)
    over = oppervlakte - int(oppervlakte / 1280) * 1280
    aantal_uur_over = int(((over / 160)*10)+0.5)/10

    print(str(aantal_personen) + " personen werken 8 uur , 1 persoon werkt " + str(math.ceil(aantal_uur_over)) + " uur.")


def main():
    oppervlakte = float(input("Geef het oppervlakte in: "))

    while oppervlakte > 0:

        bereken_aantal_werkers_en_aantal_uur(oppervlakte)
        print("Kostprijs: €" + str(bereken_kostprijs(oppervlakte)))
        oppervlakte = float(input("Geef het oppervlakte in: "))


if __name__ == '__main__':
    main()
