def teken_rechthoek(aantal_tekens, aantal_rijen):
    for i in range(aantal_rijen):
        print("* " * aantal_tekens, end="")
        print()


def main():
    aantal_tekens = int(input("Geef het aantal tekens per rij in: "))
    aantal_rijen = int(input("Geef het aantal rijen in: "))
    teken_rechthoek(aantal_tekens, aantal_rijen)


if __name__ == '__main__':
    main()
