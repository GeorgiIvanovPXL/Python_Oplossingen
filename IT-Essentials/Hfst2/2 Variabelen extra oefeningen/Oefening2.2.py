import math
diameter_wiel = int(input("Geef de diameter van een wiel in: "))
afgelegde_weg_omwenteling = diameter_wiel * math.pi * 0.0254

print("De omwenteling van het wiel is: " + str(int((afgelegde_weg_omwenteling * 100) + 0.5) / 100))

