lengte_tapijt = float(input("Geef de lengte van het tapijt (in meter) in: "))
breedte_tapijt = float(input("Geef de breedte van het tapijt (in meter) in: "))

prijs_per_vierkante_meter = float(input("Geef de prijs per m2 in:"))
plaatsingskosten = float(input("Geef de plaatsingskosten per m2 in:"))

oppervlakte = int(lengte_tapijt * breedte_tapijt * 100) / 100

kosten_tapijt = oppervlakte * prijs_per_vierkante_meter

plaatsingskosten_totaal = oppervlakte * plaatsingskosten

print("Prijs tapijt: " + str(kosten_tapijt))
print("Plaatsingskosten: " + str(plaatsingskosten_totaal))
print("Totaal: " + str(kosten_tapijt + plaatsingskosten_totaal))
