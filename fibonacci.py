def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

assert fibonacci(8) == 21
assert fibonacci(7) == 13
assert fibonacci(6) == 8
assert fibonacci(0) == 0