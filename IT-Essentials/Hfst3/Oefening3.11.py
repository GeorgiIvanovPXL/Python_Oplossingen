aantal_sterren = int(input("Geef het aantal sterren (1-5) in: "))
code = input("Code: O (enkel ontbijt), H (half-pension), V (vol pension), A (all-inclusive): ")
aantal_overnachtingen = int(input("Aantal overnachtingen: "))
seizoen = input("Seizoen: H (hoogseizoen), L (laagseizoen), T (tussenseizoen): ")

prijs_verblijf = 0
prijs_maaltijden = 0
totaal = 0

if aantal_sterren == 1:
    prijs_verblijf = 30
elif aantal_sterren == 2 or aantal_sterren == 3:
    prijs_verblijf = 40
else:
    prijs_verblijf = 55

prijs_verblijf *= aantal_overnachtingen

if code == "O":
    prijs_maaltijden = prijs_verblijf * 0.20
elif code == "H":
    prijs_maaltijden = prijs_verblijf * 0.50
elif code == "V":
    prijs_maaltijden = prijs_verblijf * 0.60
else:
    prijs_maaltijden = (prijs_verblijf * 0.60) + (80 * aantal_overnachtingen)

if seizoen == "L" and (code == "O" or code == "H"):
    totaal = (prijs_maaltijden + prijs_verblijf) - ((prijs_maaltijden + prijs_verblijf) * 0.10)
else:
    totaal = prijs_verblijf + prijs_maaltijden

print("U betaald nog maar €" + str(totaal) + " voor deze vakantie! ")
