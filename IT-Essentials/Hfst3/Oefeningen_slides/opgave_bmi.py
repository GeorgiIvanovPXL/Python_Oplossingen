lengte = float(input("Geef je lengte (in m) in:"))
gewicht = float(input("Geef je gewicht (in kg) in:"))

bmi = gewicht / (lengte * lengte)

if bmi < 18:
    print("Ondergewicht!")
elif bmi < 25:
    print("Ok.")
elif bmi < 30:
    print("Overgewicht!")
elif bmi < 40:
    print("Obesitas!")
else:
    print("Ziekelijk overgewicht!")
