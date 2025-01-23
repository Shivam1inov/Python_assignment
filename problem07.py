# Make a Simple Calculator
print("1 - Add")
print("2 - Substract")
print("3 - Multiply")
print("4 - Divide")
operation = int(input("Choose an operation : "))
result = 0
if(operation in [1,2,3,4]):
    num1= int(input("Enter first number : "))
    num2= int(input("Enter Second number : "))
    if (operation == 1):
        result = num1 + num2
    elif (operation == 2 ):
        result = num1 - num2
    elif (operation ==3):
        result = num1 * num2
    elif (operation == 4):
        result = num1 / num2
    

else:
    print("Please enter valid operation")   
print("The Result of the operation is : {}".format(result))              