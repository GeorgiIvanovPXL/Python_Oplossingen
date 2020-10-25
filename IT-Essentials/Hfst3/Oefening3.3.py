uur_vertrekken = int(input("Geef vertrekuur in: "))
min_vertrekken = int(input("Geef min. vertrek in: "))

duur = int(input("Geef de duur in: "))

aantal_uur = int(((duur / 60) + 0.5) / 1) * 1
aantal_min = duur % 60


uur_vertrekken += aantal_uur
min_vertrekken += aantal_min

uur = uur_vertrekken % 24
min = min_vertrekken % 60

print("Aankomstuur: " + str(uur) + "\nAankomstminuut: " + str(min))
