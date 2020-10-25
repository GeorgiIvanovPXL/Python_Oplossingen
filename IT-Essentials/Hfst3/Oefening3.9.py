getal1 = int(input("Geef getal 1 in: "))
getal2 = int(input("Geef getal 2 in: "))

code = int(input("Geef een code in: "))

if code == 1:
    print(getal1 + getal2)
elif code == 2:
    print(getal1 - getal2)
elif code == 3:
    print(getal1 * getal2)
elif code == 4:
    print(getal1 ** 2)
elif code == 5:
    print(getal2 ** 2)
else:
    print("Foutieve code")
