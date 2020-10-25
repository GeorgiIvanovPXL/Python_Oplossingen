afstand = int(input("Lengte van de vlucht (afstand in km):"))
klasse = int(input("Klasse: "))
prijs_ticket = 0

if afstand < 1000:
    prijs_ticket = afstand * 0.25

elif afstand < 2999:
    prijs_ticket = afstand * 0.20
else:
    prijs_ticket = afstand * 0.12

if klasse == 2:
    prijs_ticket = prijs_ticket - (prijs_ticket * 0.20)
elif klasse == 3:
    prijs_ticket = prijs_ticket + (prijs_ticket * 0.30)
else:
    prijs_ticket = prijs_ticket

print(prijs_ticket)
