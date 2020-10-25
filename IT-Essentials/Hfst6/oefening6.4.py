def vervorm_tekst(var1, var2):
    tekst_volledig = ""

    if len(var1) < 4:
        while len(var1) < 4:
            var1 += "*"
        tekst_volledig += var1
    else:

        tekst_volledig += var1[:4]

    if len(var2) < 4:
        while len(var2) < 4:
            var2 += "+"
        tekst_volledig += var2

    else:
        tekst_volledig += var2[-4:]

    return tekst_volledig


def main():
    tekst1 = input("Geef iets in: ")
    tekst2 = input("Geef nog iets in: ")

    print(vervorm_tekst(tekst1, tekst2))


if __name__ == '__main__':
    main()
