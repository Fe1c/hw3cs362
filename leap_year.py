def leap_year(year):
  if (year % 4) == 0:
    if (year % 100) == 0:
      if (year % 400) == 0:
        print("{0} is a leap year".format(year))
      else:
        print("{0} is not a leap year".format(year))
    else:
      print("{0} is a leap year".format(year))
  else:
    print("{0} is not a leap year".format(year))



while(True):   
  year = int(input("Enter year: "))
  leap_year(year)