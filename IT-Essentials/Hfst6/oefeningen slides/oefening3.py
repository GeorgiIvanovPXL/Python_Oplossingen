def print_plaatsen_klinkers(tekst):
    for i in range(len(tekst)):
        if tekst[i] in "aeiou":
            print(i, end="")


def main():
    tekst = input("Geef een woord in: ")

    print_plaatsen_klinkers(tekst)


if __name__ == '__main__':
    main()
