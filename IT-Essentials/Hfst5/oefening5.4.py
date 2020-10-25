import random


def check_getal(willekeurig, getal_gebruiker):
    if getal_gebruiker < willekeurig:
        return "Hoger"
    elif getal_gebruiker > willekeurig:
        return "Lager"
    else:
        return "Proficiat"


def main():
    aantal = 0
    willekeurig = random.randint(1, 11)
    gebruiker = int(input("Raad het getal :"))
    print(check_getal(willekeurig, gebruiker))

    while not(check_getal(willekeurig, gebruiker) == "Proficiat" or aantal >= 4):

        aantal += 1
        if aantal >= 4:
            print("Je beurten zijn op!")
        else:
            gebruiker = int(input("Raad het getal : "))
            print(check_getal(willekeurig, gebruiker))


if __name__ == '__main__':
    main()
