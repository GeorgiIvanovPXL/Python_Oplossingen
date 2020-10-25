graden_fh = float(input("Geef aantal graden Fh in: "))

graden_cls = (graden_fh - 32) * 5 / 9
print(graden_cls)

graden_cls_afgerond = int((graden_cls * 10) + 0.5) / 10
# uitkomst ==> 51.6666666666.4  * 10 5166.66666664 | 5166.666664 + 0.5 = 5167.166664 | 5167.166664 / 10 = 51.7

print("Graden Celsius = " + str(graden_cls_afgerond))
