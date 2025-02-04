# Find Armstrong Number in an Interval 

def Armstrong(num):
    power = len(str(num))
    sum = 0 
    temp = num

    while temp > 0 :
        digit = temp%10
        root = digit ** power
        sum = sum + root
        temp = temp // 10
    if sum == num :
        return True

def print_Armstrong(start, ends):
    for num in range(start, ends + 1):
        if Armstrong(num):
            print(num,end=" ")

#user input
start = int(input("enter for start range : "))
ends = int(input("enter for end range : "))
#output
print(f"Armstrong numbers between {start} and {ends} are:")
print_Armstrong(start, ends)
