import sys
import math

def quadratic(a, b, c):
    if a == 0:
        raise ValueError("Not a valid quadratic: the leading coefficient cannot be zero.\n")
    disc = b**2 - 4*a*c
    if disc < 0:
        raise ValueError("There are no real solutions.\n")
    else:
        return (-b + math.sqrt(disc)) / (2*a), (-b - math.sqrt(disc)) / (2*a)


try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])

    try:
        x_1, x_2 = quadratic(a, b, c)
        if x_1 == x_2:
            print('The equation {}x^2 + {}x + {} = 0 has one solution:'.format(a, b, c))
            print('x = {:.2f}\n'.format(x_1))
        else:
            print('The equation {}x^2 + {}x + {} = 0 has two solutions:'.format(a, b, c))
            print('x = {:.2f} and x = {:.2f}\n'.format(x_1, x_2))

    except ValueError as e:
        print(e)

except ValueError:
    print("The coefficients must be integers.\n")
except IndexError:
    print("A quadratic needs three coefficients.\n")

