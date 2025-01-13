# Python program to find the largest among three numbers 
num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))
num3 = int(input("enter Third number :"))
if num1 > num2 and num1 > num3 :
    print(num1,"is largest number.")
elif num2 > num1 and num2 > num3 :
    print(num2,"is largest number.")
elif num3 > num2 and num3 > num1 :
    print(num3,"is largest number.")
elif num1 == num2 == num3 :
    print("All are equal")
elif num1 == num2 :
    print("first and second number are equal")
elif num1 == num3 :
    print("first and third number are equal")
elif num2 == num3 :
    print("second and third are equal")
else :
    print("please enter valid number")