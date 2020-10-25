prijs_boek = 24.95
korting_boekwinkels = 0.4
kosten_per_boek = 0.75
aantal_boeken = 60

# 60 boeken kostprijs

print("De winkel betaalt " +
      str(((prijs_boek * aantal_boeken) - (prijs_boek * aantal_boeken) * korting_boekwinkels) +
          (3 + ((aantal_boeken - 1) * kosten_per_boek))))
