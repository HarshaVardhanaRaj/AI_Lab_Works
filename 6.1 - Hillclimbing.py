import random
import math

def f(x):
    return -(x - 3) ** 2 + 9

def hill_climbing():
    x = random.randint(-10, 10)

    while True:
        current = f(x)

        left = f(x - 1)
        right = f(x + 1)

        if left > current:
            x -= 1
        elif right > current:
            x += 1
        else:
            break

    return x, f(x)

x1, value1 = hill_climbing()
print("Hill Climbing:")
print("x =", x1, "Value =", value1)
