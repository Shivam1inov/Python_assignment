# Write a Python program of recursion list sum
def recursive_sum(lst):
   
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[1:])

num = [1,2,3,4,5,6,7,8,9]
print(num)
print("The sum of the list is:", recursive_sum(num))
