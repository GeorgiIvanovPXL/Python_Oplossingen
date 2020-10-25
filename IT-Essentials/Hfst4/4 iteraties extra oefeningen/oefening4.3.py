def bereken_gemiddelde(naam, test1, test2, test3):
    gemiddelde = (test1 + test2 + test3) / 3

    if gemiddelde < 70:
        print(naam + " Test 1: " + str(test1) + " Test 2: " + str(test2) + " Test 3: " + str(test3) + " gemiddelde: " + str(gemiddelde) + " Resultaat: faalt")
    else:

        print(naam + " Test 1: " + str(test1) + " Test 2: " + str(test2) + " Test 3: " + str(test3) + " gemiddelde: " + str(gemiddelde) + " Resultaat: slaagt")


def main():
    naam = input("Geef de naam in: ")
    while not(naam == "xx" or naam == "XX"):
        test1 = int(input("Geef resultaat 1 in: "))
        test2 = int(input("Geef resultaat 2 in: "))
        test3 = int(input("Geef resultaat 3 in: "))
        bereken_gemiddelde(naam, test1, test2, test3)
        naam = input("Geef de naam in: ")


if __name__ == '__main__':
    main()
