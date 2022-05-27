#Taking input from user
year = int(input("\nEnter any Year:"))

#if-elif loop is used here to find the leap year.
if year%4 == 0 and year%100 !=0:
    print(year, "is a Leap Year")
elif year%400 ==0:
    print(year, "is a Leap Year")
else:
    print(year, "is not an Leap Year")
