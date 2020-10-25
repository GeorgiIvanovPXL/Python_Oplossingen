percentage_maan = float(input("Percentage Maan: "))
percentage_jupiter = float(input("Percentage Jupiter: "))
percentage_mars = float(input("Percentage Mars: "))

for i in range(50, 121, 5):
    print("Aarde: " + str(i))
    print("Maan: " + str(i * (percentage_maan / 100)))
    print("Jupiter: " + str(i * (percentage_jupiter / 100)))
    print("Mars: " + str(i * (percentage_mars / 100)))
    print()

