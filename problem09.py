# Print all Prime Numbers in an Interval

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes_in_interval(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

# user Input
start = int(input("enter of start range : "))
end = int(input("enter of end range : "))
print(f"Prime numbers between {start} and {end} are:")
print_primes_in_interval(start, end)
