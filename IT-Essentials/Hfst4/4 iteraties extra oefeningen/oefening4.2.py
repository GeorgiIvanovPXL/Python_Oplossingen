def bereken_graad(naam, gemiddelde):

    if gemiddelde < 60:
        print(str(naam) + " onvoldoende!")
    elif gemiddelde < 70:
        print(str(naam) + " voldoende!")
    elif gemiddelde < 80:
        print(str(naam) + " onderscheiding!")
    elif gemiddelde < 85:
        print(str(naam) + " grote onderscheiding!")
    else:
        print(str(naam) + " grootste onderscheiding!")


def main():
    naam = input("Geef de naam in: ")

    while not(naam == "xx" or naam == "XX"):
        percentage = float(input("Geef percentage in: "))
        bereken_graad(naam, percentage)
        naam = input("Geef de naam in: ")


if __name__ == '__main__':
    main()




