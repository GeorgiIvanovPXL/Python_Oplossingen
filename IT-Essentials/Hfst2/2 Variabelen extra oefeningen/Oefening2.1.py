BTW = 1.21
kost_gesprek_binnenland = 12
kost_gesprek_buitenland_per_min = 50

aantal_gesprekken_binnenland = int(input("Aantal gesprekken binnen België: "))
aantal_min_buitenland = int(input("Aantal min. (buitenlandse gesprekken) : "))

bedrag = int((((aantal_gesprekken_binnenland * kost_gesprek_binnenland) +
               (aantal_min_buitenland * kost_gesprek_buitenland_per_min) * BTW) / 100 * 100) + 0.5) / 100

print("Je hebt een openstaand bedrag van €" + str(bedrag) +
      " voor de afgelopen maand!")


