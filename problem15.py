#Print the Fibonacci sequence 

a = 0 
b = 1
num = int(input("Enter for num : "))
if num == 1:
    print(a)
else:
    print(a ,end=" ")
    print(b , end=" ")
    for i in range(2,num):
        c = a + b
        a = b 
        b = c 
        print(c,end=" ")
print("this is fibonacci sequence.")