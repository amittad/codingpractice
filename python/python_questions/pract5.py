# accept the year and check year is leap or not
year = int(input("enter the year=="))

if year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")