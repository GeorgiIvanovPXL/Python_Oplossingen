artikels = ""
totaal = 0
artikelnummer = int(input("Geef artikelnummer in: "))

while artikelnummer != 999:
    hoeveelheid = int(input("Geef hoeveelheid in: "))
    eenheidsprijs = float(input("Geef de eenheidsprijs in: "))
    bedrag = eenheidsprijs * hoeveelheid
    artikels += "Artikelnummer: " + str(artikelnummer) + "   Hoeveelheid " + str(hoeveelheid) + "   Eenheidsprijs" + str(eenheidsprijs) + "   Bedrag " + str(bedrag) + "\n"
    totaal += bedrag
    artikelnummer = int(input("Geef artikelnummer in: "))

print(artikels)
print("Totaal = " + str(totaal))





