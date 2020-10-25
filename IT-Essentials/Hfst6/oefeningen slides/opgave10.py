def make_simple(string):
    tekst = ""
    for letter in string:
        if ord(letter) not in range(97, 123):
            tekst += ""
        else:
            tekst += letter

    return tekst


def main():
    string = input("Geef iets in: ")
    print(make_simple(string))


if __name__ == '__main__':
    main()
