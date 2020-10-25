def vervorm_tekst(string):
    tekst = string.strip()[string.find("#") + 1:]
    return tekst


def main():
    string = "Barefoot on the grass, listening to our favorite song."

    print(vervorm_tekst(string))


if __name__ == '__main__':
    main()