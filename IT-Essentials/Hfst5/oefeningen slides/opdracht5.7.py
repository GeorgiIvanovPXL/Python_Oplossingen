def toon_tafel(getal):
    for i in range(0, 11, 1):
        print(str(i) + " x " + str(getal) + " = " + str(i * getal))


def main():
        tafel = int(input("Welke tafel wil je zien? : "))
        toon_tafel(tafel)


if __name__ == '__main__':
    main()
