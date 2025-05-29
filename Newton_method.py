import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.cos(x) - x

def f_prime(x):
    return -np.sin(x) - 1

def newton_method(f, f_prime, x0, tolerance=1e-10, max_iter=100):
    x_values = [x0]
    for _ in range(max_iter):
        x_new = x_values[-1] - f(x_values[-1]) / f_prime(x_values[-1])
        x_values.append(x_new)
        if abs(x_new - x_values[-2]) < tolerance:
            break
    return x_values

initial_guess = 1.0
roots = newton_method(f, f_prime, initial_guess)

true_root = roots[-1]
errors = [abs(x - true_root) for x in roots]

plt.figure(figsize=(10, 5))
plt.plot(range(len(roots)), roots, marker='o', label="Newton Bop")
plt.axhline(y=true_root, color='gray', linestyle='--', label="ZZIN root")
plt.xlabel("repeat")
plt.ylabel("x value")
plt.title("Newton Bop cos(x) = x")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(range(len(errors)), errors, marker='o', color='red', label="ZZIN O ")
plt.yscale("log")
plt.xlabel("repeat")
plt.ylabel("O Cha")
plt.title("Newton Bop O Cha")
plt.legend()
plt.grid(True)
plt.show()
