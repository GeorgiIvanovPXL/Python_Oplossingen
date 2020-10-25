import math
diameter_wiel = int(input("Geef de diameter van een wiel in: "))
aantal_meter = float(input("Geef de af te leggen afstand in: "))
afgelegde_weg_omwenteling = diameter_wiel * math.pi * 0.0254

aantal_omwentelingen = int(((aantal_meter / afgelegde_weg_omwenteling) * 100) + 0.5) / 100

print("Aantal omwentelingen nodig om " + str(aantal_meter) + " meter af te leggen: " + str(aantal_omwentelingen))
