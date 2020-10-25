def prog(naam,voornaam ):

    nieuwe_naam = voornaam[0].upper() + ". " + naam[0].upper() + naam[1:]

    return nieuwe_naam


def main():
    naam = input("Geef je naam in: ")
    voornaam = input("Geef je voornaam in: ")
    print(prog(naam, voornaam))


if __name__ == '__main__':
    main()
