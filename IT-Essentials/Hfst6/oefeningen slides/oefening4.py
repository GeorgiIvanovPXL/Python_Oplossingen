def print_gelijkenissen():
    tekst1 = "Georgiouszen"
    tekst2 = "Giogriiuzzin"

    for i in range(len(tekst1)):  # van 0 tot lengte van "Georgi"
        if tekst1[i] in tekst2:   # als er een letter van "Georgi" terugkomt in "Giogri"
            for j in range(len(tekst2)):  # van 0 tot lengte van "Giogri"
                if tekst1[i] == tekst2[j] and i == j:  # als letters  gelijk zijn en indexen "i en j" gelijk zijn
                    print("Letter: " + tekst1[i] + "\nIndex: " + str(i))


def main():
    print_gelijkenissen()


if __name__ == '__main__':
    main()

