import math
straal = float(input("Geef straal in: "))

oppervlakte_cirkel = straal ** 2 * math.pi
oppervlakte_cirkel_afgerond = int((oppervlakte_cirkel * 100) + 0.5) / 100

print("De oppervlakte van een cirkel met straal " + str(straal) + " is " + str(oppervlakte_cirkel_afgerond))


