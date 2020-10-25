def bepaal_n(n):
    if ord(n) in range(65, 91):
        return "Hoofdletter"
    elif ord(n) in range(97, 123):
        return "Kleinletter"
    elif ord(n) in range(48, 57):
        return "Nummer"
    else:
        return "Onbekend"


def main():
    som = 0
    n = input("Geef iets in: ")
    while not bepaal_n(n) == "Onbekend":
        print(bepaal_n(n))
        if bepaal_n(n) == "Nummer":
            som += int(n)
        n = input("Geef iets in: ")

    print(som)


if __name__ == '__main__':
    main()
