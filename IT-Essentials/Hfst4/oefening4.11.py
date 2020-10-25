personeelsnummer = int(input("Personeelsnummer: "))

aantal_man = 0
aantal_vrouw = 0

while personeelsnummer != 0:
    geslacht = int(input("Geslacht (0=vrouw; 1=man) :"))
    leeftijd = int(input("Leeftijd: "))
    brutoloon = int(input("Brutoloon: "))
    if geslacht == 1 and (leeftijd > 34 or brutoloon >= 1800):
        aantal_man += 1
    if geslacht == 0 and leeftijd < 25:
        aantal_vrouw += 1
    personeelsnummer = int(input("Personeelsnummer: "))

print("Aantal mannen ouder dan 34 of loon hoger dan 1800: " + str(aantal_man))
print("Aantal vrouwen jonger dan 25 jaar: " + str(aantal_vrouw))
