prijs_volwassenen = 11
prijs_kinderen = 6

aantal_volwassenen = int(input("Geef het aantal volwassenen in: "))
aantal_kinderen = int(input("Geef het aantal kinderen in (onder 12): "))

prijs = (aantal_volwassenen * prijs_volwassenen) + (aantal_kinderen * prijs_kinderen)

print("De toegangsprijs bedraagt: " + " € " + str(prijs))
