#  Python Program to Display Fibonacci Sequence Using Recursion 
def fibon(n):
    if n<=1:
        return n
    else:
        return fibon(n-1)+fibon(n-2)
    
n = int(input("Enter a number for fibonacci sequence : "))
print("fibonacci sequence :")
for i in range(n):
    print(fibon(i),end = " ")
