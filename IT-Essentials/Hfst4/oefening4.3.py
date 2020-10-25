som = 0
aantal_negatief = 0

invoer = int(input("Geef een getal in: "))
while invoer != 0:
    if invoer < 0:
        aantal_negatief += 1
    som += invoer
    invoer = int(input("Geef een getal in: "))

print("Som = " + str(som))
print("Aantal negatieve getallen = " + str(aantal_negatief))
