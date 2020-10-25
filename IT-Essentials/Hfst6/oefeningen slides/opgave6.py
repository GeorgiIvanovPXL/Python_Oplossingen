def print_middelste(tekst):
    if len(tekst) % 2 == 0:
        print(tekst[int(len(tekst) / 2 - 1):int(len(tekst) / 2 + 1)])
    else:
        print(tekst[int(len(tekst) / 2)])


def main():
    tekst = input("Geef een tekst in: ")
    print_middelste(tekst)


if __name__ == '__main__':
    main()
