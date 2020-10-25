leeftijd = int(input("Geef je leeftijd in: "))
burgerlijke_staat = int(input("Geef burgerlijke staat in: (1 = ongehuwd, 2 = gehuwd, 3 = weduw(e)(naar)): "))

lidgeld = 0

if burgerlijke_staat == 1 and leeftijd < 30:
    lidgeld = 25
else:
    lidgeld = 15

print("Jouw jaarlijkse lidmaatschap bedraagt: " + str(lidgeld))
