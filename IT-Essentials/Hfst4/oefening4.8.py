inschrijvingsnummer = int(input("Inschrijvingsnummer: "))
kleinste_tijd = 99999
meer_dan_een_uur = 0
snelste_inschrijvingsnummer = 0
aantal = 0
while inschrijvingsnummer > 0:
    tijd = int(input("Tijd v.d rit: "))
    if tijd < kleinste_tijd:
        kleinste_tijd = tijd
        snelste_inschrijvingsnummer = inschrijvingsnummer
    if tijd > 3600:
        meer_dan_een_uur += 1

    aantal += 1
    inschrijvingsnummer = int(input("Inschrijvingsnummer: "))

meer_dan_een_uur = (meer_dan_een_uur / aantal) * 100

uren_snelste = kleinste_tijd // 3600
rest = kleinste_tijd % 3600

minuten_snelste = rest // 60
rest = rest % 60
seconden_snelste = rest

print("Snelste renner is de renner met inschrijvingsnummer: " + str(snelste_inschrijvingsnummer))
print("Het percentage van de renners dat er langer dan 1 uur over doet: %" + str(meer_dan_een_uur))
print("Snelste: uren " + str(uren_snelste) + ", minuten " + str(minuten_snelste) + ", seconden " + str(seconden_snelste))

