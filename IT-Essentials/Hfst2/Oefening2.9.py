aantal_centen = int(input("Geef het aantal centen in: "))

aantal_twee_euro = int(aantal_centen / 200)
rest = aantal_centen % 200 # rest = 159

aantal_euro = int(rest / 100)
rest = aantal_centen % 100 # rest = 59

aantal_vijftig_cent = int(rest / 50)
rest = aantal_centen % 50

aantal_twintig_cent = int(rest / 20)
rest = aantal_centen % 20

aantal_tien_cent = int(rest / 10)
rest = aantal_centen % 10

aantal_vijf_cent = int(rest / 5)
rest = aantal_centen % 5

aantal_twee_cent = int(rest / 2)
rest = aantal_centen % 2

aantal_één_cent = int(rest / 1)

print(str(aantal_centen) + " centen = " + str(aantal_twee_euro) + " X 2 euro \n" +
      "" + str(aantal_euro) + " X 1 euro \n" +
      "" + str(aantal_vijftig_cent) + " X 50 cent \n" +
      "" + str(aantal_twintig_cent) + " X 20 cent \n" +
      "" + str(aantal_tien_cent) + " X 10 cent \n" +
      "" + str(aantal_vijf_cent) + " X 5 cent \n" +
      "" + str(aantal_twee_cent) + " X 2 cent \n" +
      "" + str(aantal_één_cent) + " X 1 cent")



