getal1 = int(input("Geef getal 1 in: "))
getal2 = int(input("Geef getal 2 in: "))

kleinste = 0
grootste = 0

if getal1 < getal2:
    kleinste = getal1
    grootste = getal2

else:
    kleinste = getal2
    grootste = getal1

kwadraat_kleinste = kleinste ** 2


deling = grootste / kleinste

print("Kwadraat kleinste: " + str(kwadraat_kleinste) + "\nDeling: " + str(deling))
