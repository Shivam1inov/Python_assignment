#Find Sum of Natural Numbers Using Recursion
def sum(x):
    if (x==1):
        return 1
    else:
        return (x + sum(x-1))

x = int(input("enter a valid number : "))
print("sum of",x,"natural number : ",sum(x))