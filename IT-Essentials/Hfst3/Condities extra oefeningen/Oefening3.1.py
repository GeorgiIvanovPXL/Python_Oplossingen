a = float(input("Geef getal a in: "))
b = float(input("Geef getal b in: "))
c = float(input("Geef getal c in: "))

som = a + b

if som < 20:
    som = a + b + c
    print(som)
else:
    print("Te groot!")
