BTW_PERCENTAGE = 0.21
eenheidsprijs = 11.5
korting_boven_duizend = 0.10
aantal = int(input("Geef het gewenste aantal artikels in: "))

bedrag = (eenheidsprijs * aantal) * (1 + BTW_PERCENTAGE)

if bedrag > 1000:
    bedrag -= bedrag * korting_boven_duizend

print("Bedrag: " + str(bedrag))






