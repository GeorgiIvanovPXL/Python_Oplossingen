jaar_film = int(input("Geef het jaar in: "))
rating_film = int(input("Rating (1-5) :"))
basisprijs = 5
prijs = 0
jaartal_verschil = 2020 - jaar_film

if jaartal_verschil < 2:
    basisprijs += 1

if rating_film == 2 or rating_film == 3:
    basisprijs += 1
elif rating_film == 4 or rating_film == 5:
    basisprijs += 2

if basisprijs > 7:
    basisprijs = 7

print("Bedrag: " + str(basisprijs))
