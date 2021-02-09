def factorial_iterative(n):
    i = 1
    x = 1
    while x <= n:
        i *= x
        x += 1
    return i

assert factorial_iterative(4) == 24
assert factorial_iterative(3) == 6
assert factorial_iterative(2) == 2
assert factorial_iterative(1) == 1
assert factorial_iterative(0) == 1

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)

print(factorial_iterative(10000))
print(factorial_recursive(10000))