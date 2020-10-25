def vervorm_tekst(string):
    if len(string) % 2 == 0:
        if "t" or "T" in string:
            positie = string.find('t')
            string = string[0:positie] + string[positie:].lower()
        else:
            print("Geen 't' of 'T'  in tekst!")
    else:
        if "t" or "T" in string:
            positie = string.find('t')
            string = string[0:positie] + string[positie:].upper()
        else:
            print("Geen 't' of 'T'  in tekst!")

    return string


def main():

    tekst = input("Geef een tekst in: ")
    print(vervorm_tekst(tekst))


if __name__ == '__main__':
    main()
