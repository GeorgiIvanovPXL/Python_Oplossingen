som = 0
hoogste_temp = 0
for i in range(10):
    temperatuur = float(input("Temperatuur dag " + str(i + 1) + " : "))
    if temperatuur > hoogste_temp:
        hoogste_temp = temperatuur
    som += temperatuur
gemiddelde = som / 10

print("Gemiddelde temperatuur voor de laatste 10 dagen: " + str(gemiddelde))
print("Hoogste temperatuur: " + str(hoogste_temp))

