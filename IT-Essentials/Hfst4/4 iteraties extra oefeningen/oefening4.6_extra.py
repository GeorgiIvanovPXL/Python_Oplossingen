def teken_rand_rechthoek(aantal_tekens, aantal_rijen):
    for i in range(aantal_rijen):
        if i == 0:
            print("* " * aantal_tekens, end="")
            print()
        elif i == aantal_rijen - 1:
            print("* " * aantal_tekens, end="")
        else:
            print("* " + "  " * (aantal_tekens - 2) + "*")


def main():
    aantal_tekens = int(input("Geef het aantal tekens per rij in: "))
    aantal_rijen = int(input("Geef het aantal rijen in: "))
    teken_rand_rechthoek(aantal_tekens, aantal_rijen)


if __name__ == '__main__':
    main()
