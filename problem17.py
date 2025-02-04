# Check Armstrong Number
num = int(input("Enter a number for armstrong number: "))
power = len(str(num))
sum = 0 
temp = num

while temp > 0 :
    digit = temp%10
    root = digit ** power
    sum = sum + root
    temp = temp // 10

if sum == num :
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")