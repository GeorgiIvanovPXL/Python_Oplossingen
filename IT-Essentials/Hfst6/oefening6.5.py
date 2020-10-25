def bepaal_prijs(volwassenen, kinderen, hotelcode, aantal_sterren, kindercode):
    prijsvolwassenen = 0
    prijskinderen = 0
    if aantal_sterren == 1 or aantal_sterren == 2:
        prijsvolwassenen = 48
    elif aantal_sterren == 3:
        if hotelcode[:2] == "BR" or hotelcode[:2] == "AN":
            prijsvolwassenen = 60
        else:
            prijsvolwassenen = 56

    else:
        prijsvolwassenen = 60

    if hotelcode[:2] == "HI":
        prijsvolwassenen = 70

    if kindercode == "A":
        if(aantal_sterren == 1 or aantal_sterren == 2) or hotelcode[:2] != "BR":
            prijskinderen = 0

    else:
        prijskinderen = prijsvolwassenen / 2

    return str.format("{:12} {} {:5} {}", hotelcode + "*" * aantal_sterren, str(prijsvolwassenen),  str(prijskinderen), str((volwassenen * prijsvolwassenen) + (kinderen * prijskinderen)))


def main():
    hotels_en_prijzen = ""
    hotelcode = input("Hotelcode: ")
    while hotelcode != "/":
        aantal_volwassenen = int(input("Geef het aantal volwassenen in: "))
        aantal_kinderen = int(input("Geef het aantal kinderen in: "))
        aantal_sterren = int(input("Geef het aantal sterren in: "))
        kindercode = input("Kindercode: ")

        while ord(kindercode) not in range(65, 91):
            kindercode = input("Kindercode ('A' t.e.m. 'Z' is toegelaten): ")
        hotels_en_prijzen += bepaal_prijs(aantal_volwassenen, aantal_kinderen, hotelcode, aantal_sterren, kindercode) + "\n"
        hotelcode = input("Hotelcode: ")

    print(hotels_en_prijzen)


if __name__ == '__main__':

    main()
