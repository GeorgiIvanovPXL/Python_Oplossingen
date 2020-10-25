leeftijd = int(input("Geef leeftijd in: "))
lidgeld = 0

if leeftijd < 12:
    lidgeld = 6
elif leeftijd < 18:
    lidgeld = 12.5
else:
    lidgeld = 25

print("Leeftijd: " + str(leeftijd) + "\nLidgeld: " + str(lidgeld))
