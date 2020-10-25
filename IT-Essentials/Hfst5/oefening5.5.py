def controleer(lidnummer):
    cijfers = int(str(lidnummer)[1] + str(lidnummer)[3])
    laatste = int(str(lidnummer)[5] + str(lidnummer)[6])

    if cijfers == laatste:
        print("gratis")
    else:
        print("niet gratis")


def main():
    lidnummer = int(input("Geef lidnummer in: "))
    controleer(lidnummer)


if __name__ == '__main__':
    main()
