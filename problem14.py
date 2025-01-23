# Find Factors of Number
a = int(input("Enter a number : "))
for i in range(1, a+1):
    if a % i == 0 :
        print( "factor of a : ", i)