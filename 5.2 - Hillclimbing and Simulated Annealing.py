import random
import math

# Function to maximize
def f(x):
    return -(x - 3) ** 2 + 9


# ---------------- HILL CLIMBING ----------------
def hill_climbing():
    x = random.randint(-10, 10)

    while True:
        current = f(x)

        # Check both neighbours
        left = f(x - 1)
        right = f(x + 1)

        # Move to the better neighbour
        if left > current:
            x -= 1
        elif right > current:
            x += 1
        else:
            break

    return x, f(x)


# ---------------- SIMULATED ANNEALING ----------------
def simulated_annealing():
    x = random.randint(-10, 10)
    temperature = 100

    while temperature > 0.1:

        # Generate a neighbouring solution
        new_x = x + random.choice([-1, 1])

        current = f(x)
        new_value = f(new_x)

        # If better, accept it
        if new_value > current:
            x = new_x

        # If worse, sometimes accept it
        else:
            probability = math.exp((new_value - current) / temperature)

            if random.random() < probability:
                x = new_x

        # Reduce temperature
        temperature *= 0.95

    return x, f(x)


# Run algorithms
x1, value1 = hill_climbing()
x2, value2 = simulated_annealing()

print("Hill Climbing:")
print("x =", x1, "Value =", value1)

print("\nSimulated Annealing:")
print("x =", x2, "Value =", value2)