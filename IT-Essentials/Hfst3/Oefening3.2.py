brutoloon = float(input("Geef het brutoloon in: "))
jaarlijkse_bijdrage = 0
vakantiegeld = brutoloon * 0.05

if vakantiegeld >= 350:
    jaarlijkse_bijdrage = 350 * 0.08
else:
    jaarlijkse_bijdrage = vakantiegeld * 0.08


print("Brutoloon: " + str(brutoloon) + "\nVakantiegeld: "+str(vakantiegeld)+ "\nJaarlijkse bijdrage: " + str(jaarlijkse_bijdrage))
