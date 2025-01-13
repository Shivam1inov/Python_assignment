# python program to check leap year
year = int(input("Enter year :"))
if (year-1)%4 == 0 :
    print(year,"is leap year")
else :
    print(year,"is not a leap year")