def print_tekens(teken, aantal):
    print(teken * aantal)


def maak_rechthoek(hoogte, breedte, teken):
    for i in range(hoogte):
        print_tekens(teken, breedte)


maak_rechthoek(4, 7, "*")
