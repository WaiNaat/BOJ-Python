from math import sqrt, floor

# functions
def is_palindrome(val):
    val = str(val)
    for i in range(len(val) // 2):
        if val[i] != val[-1 - i]:
            return False
    return True

def is_prime(val):
    if val == 1: return False
    for i in range(2, floor(sqrt(val)) + 1):
        if val % i == 0:
            return False
    return True

# input
n = int(input())

# process
found = False
while not found:
    if is_palindrome(n) and is_prime(n):
        found = True
    else:
        n += 1

# output
print(n)