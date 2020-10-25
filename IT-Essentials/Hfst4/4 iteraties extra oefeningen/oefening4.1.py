def bereken_prijs_jetons():
    prijs = 0.7

    for i in range(1, 51, 1):
        print(str(i) + " jeton(s) = " + str(int(((prijs * i) * 10) + 0.5) / 10))


def main():
    bereken_prijs_jetons()


if __name__ == '__main__':
    main()
