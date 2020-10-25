HUIDIG_JAAR = 2020

leeftijd = int(input("Geef leeftijd in: "))
aansluitingsjaar = int(input("Geef het aansluitingsjaar in: "))

basisbedrag = 100

if leeftijd < 21 or leeftijd > 60:
    basisbedrag -= 14.5

reductie = 2.5 * (HUIDIG_JAAR - aansluitingsjaar)

basisbedrag -= reductie

if basisbedrag < 62.5:
    basisbedrag = 62.5


print("Bedrag: " + str(basisbedrag))
