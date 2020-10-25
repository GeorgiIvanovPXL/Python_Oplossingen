som = 0
for i in range(28):
    leeftijd = int(input("Geef leeftijd van student " + str(i+1) + " in: "))
    som += leeftijd

gemiddelde = som / (i + 1)

print("Gemiddelde leeftijd " + str(gemiddelde) + ".")

