year = int(input("Enter the year you want to check: "))

if year%4 == 0:
    if year%100 ==0:
       if year%400 == 0:
        print(f"the year {year} is a leap year ")
       else:
        print(f"the year {year} is a not leap year ")
    else:
      print(f"the year {year} is a leap year ")
else:
    print(f"the year {year} is not a leap year")