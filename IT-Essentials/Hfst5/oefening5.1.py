def euro_to_usd(ex_rate, amount):
    print("$" + str(amount * ex_rate))


def main():
    waarde = float(input("Geef de waarde van de euro in t.o.v. de US dollar: "))
    bedrag = float(input("Geef het bedrag in: "))
    while bedrag != 0:
        euro_to_usd(waarde, bedrag)
        bedrag = float(input("Geef het bedrag in: "))


if __name__ == '__main__':
    main()
