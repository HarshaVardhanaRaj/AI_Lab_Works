import random
import math

def simulated_annealing():
    x = random.randint(-10, 10)
    temperature = 100

    while temperature > 0.1:
        new_x = x + random.choice([-1, 1])

        current = f(x)
        new_value = f(new_x)

        if new_value > current:
            x = new_x
        else:
            probability = math.exp((new_value - current) / temperature)

            if random.random() < probability:
                x = new_x

        temperature *= 0.95
    return x, f(x)

x2, value2 = simulated_annealing()
print("\nSimulated Annealing:")
print("x =", x2, "Value =", value2)
