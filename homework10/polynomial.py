#this code is heavily refrenced from chatgpt, and have learned how it works
import random

def hillClimbing(f, p, h=0.01):
    failCount = 0
    while failCount < 10000:
        fnow = abs(f(p))  # Absolute value for finding roots
        fneighbor = p.copy()
        for i in range(len(fneighbor)):
            fneighbor[i] += random.choice([-h, h, 0])
        fneighbornow = abs(f(fneighbor))  # Absolute value for finding roots

        if fneighbornow < fnow:
            p = fneighbor.copy()
            print('p =', p, 'f(p) =', f(p))
            failCount = 0
        else:
            failCount += 1

        if fnow < 0.001:
            break

    return p, fnow

def polynomial_solver(coefficients):
    def polynomial_function(p):
        return sum(coef * p[0] ** i for i, coef in enumerate(coefficients[::-1]))
    return polynomial_function

# Example usage:

# Polynomial: x^5 + 1 = 0
coefficients = [1, 0, 0, 0, 0, 1]
root, value = hillClimbing(polynomial_solver(coefficients), [0])
print(f"Approximate root: {root}, Value at root: {value}")

# Polynomial: x^8 + 3x^2 + 1 = 0
coefficients = [1, 0, 0, 0, 0, 0, 0, 3, 1]
root, value = hillClimbing(polynomial_solver(coefficients), [0])
print(f"Approximate root: {root}, Value at root: {value}")
