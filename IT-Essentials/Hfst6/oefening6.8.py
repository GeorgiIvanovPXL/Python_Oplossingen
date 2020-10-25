def print_driehoek(grootte, begin_letter):
    tekst = ""
    for i in range(0, grootte + 1):
        for j in range(0, i):
            tekst += chr(ord(begin_letter))
            begin_letter = chr(ord(begin_letter) + 1)
            if ord(begin_letter) > 90:
                begin_letter = "A"

        print(tekst)
        tekst = ""

    print()


def main():
    grootte = int(input("Geef grootte in: "))
    letter = input("Geef het beginletter in: ")
    print_driehoek(grootte, letter)


if __name__ == '__main__':
    main()
