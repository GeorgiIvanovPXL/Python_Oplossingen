resultaat_1 = int(input("Geef resultaat 1 in: "))
resultaat_2 = int(input("Geef resultaat 2 in: "))
resultaat_3 = int(input("Geef resultaat 3 in: "))

gemiddelde = (resultaat_1 + resultaat_2 + resultaat_3) / 3

percentage = (gemiddelde / 20) * 100

if percentage < 60:
    print("Onvoldoende!")
elif percentage < 70:
    print("Voldoende!")
elif percentage < 80:
    print("Onderscheiding!")
elif percentage < 90:
    print("Grote onderscheiding!")
else:
    print("Grootste onderscheiding!")
