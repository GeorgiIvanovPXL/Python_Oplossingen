gewicht_appel = int(input("Geef het gewicht van een appel (in gram) in: "))
for i in range(1, 101, 1):
    print(str(i) + " appel(s) = " + str(gewicht_appel * i) + " gr.")

