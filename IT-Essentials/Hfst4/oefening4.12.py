familienaam = input("Familienaam: ")
premie = 0
alles = ""
totaal_premie = 0
hoogste_premie = 0
while not(familienaam == "/" or familienaam == "\*"):
    voornaam = input("Voornaam: ")
    aantal_dienstjaren = int(input("Aantal dienstjaren: "))
    while aantal_dienstjaren < 0 or aantal_dienstjaren > 40:
        print("Aantal dienstjaren moet tussen 0 en 40 zijn!")
        aantal_dienstjaren = int(input("Aantal dienstjaren: "))

    if aantal_dienstjaren < 5:
        premie = 0
    else:
        premie = aantal_dienstjaren * 25

    if premie > hoogste_premie:
        hoogste_premie = premie

    totaal_premie += premie
    alles += "Familienaam: " + familienaam + " Voornaam: " + voornaam + " Aantal dienstjaren: "\
             + str(aantal_dienstjaren) + " Premie: " + str(premie) + "\n"
    print(alles)
    familienaam = input("Familienaam: ")


print("Totaal te betalen premie: " + str(totaal_premie))
print("Hoogste premie: " + str(hoogste_premie))
