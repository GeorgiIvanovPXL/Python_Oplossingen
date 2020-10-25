def change_letters(string):
    aantal_o = 0

    tekst = string.replace('a', 'o')

    for letter in tekst:
        if letter == "o":
            aantal_o  += 1

    print(tekst)
    print(aantal_o)


def main():
    string = "abracadabra"
    change_letters(string)



if __name__ == '__main__':
    main()