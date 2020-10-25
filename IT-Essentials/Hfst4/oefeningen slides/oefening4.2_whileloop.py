som = 0
gemiddelde = 0
aantal = 0

while aantal < 28:
    leeftijd = int(input("Geef de leeftijd van dtudent " + str(aantal + 1) + " in: "))
    som += leeftijd
    aantal += 1

gemiddelde = som / (aantal + 1)

print("Gemiddelde leeftijd = " + str(int(gemiddelde)))

