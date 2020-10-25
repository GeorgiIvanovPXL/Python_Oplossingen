def druk_lengte_af(string):

    return len(string)


def main():
    tekst = input("Geef een woord in: ")
    print(str(druk_lengte_af(tekst)))


if __name__ == '__main__':
    main()