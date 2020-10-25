import random


def genereer_huiswerk():

    aantal_reeksen = 0

    while aantal_reeksen < 5:
        for i in range(5):
            print("reeks " + str(i+1))
            for j in range(5):
                getal1 = random.randint(0, 20)
                getal2 = random.randint(0, 20)
                if getal1 - getal2 < 0:
                    while getal1 - getal2 < 0:
                        getal1 = random.randint(0, 20)
                        getal2 = random.randint(0, 20)
                print(str(j + 1) + ") " + str(getal1) + " - " + str(getal2) + " =")
            aantal_reeksen += 1
            print()


def main():
    genereer_huiswerk()


if __name__ == '__main__':
    main()
