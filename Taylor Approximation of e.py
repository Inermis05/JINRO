import numpy as np
import matplotlib.pyplot as plt
import math

def taylor_exp(x, n_terms):
    return sum((x**k) / math.factorial(k) for k in range(n_terms + 1))

true_e = np.exp(1)

n_range = range(1, 21)
approximations = [taylor_exp(1, n) for n in n_range]
errors = [abs(true_e - approx) for approx in approximations]

plt.figure(figsize=(10, 5))
plt.plot(n_range, approximations, label="Taylor Approximation of e")
plt.axhline(y=true_e, color='gray', linestyle='--', label="True value of e")
plt.xlabel("Number of terms in Taylor series")
plt.ylabel("Approximated value")
plt.title("Convergence of Taylor Series for e^1")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(n_range, errors, label="ZoalThea O Cha", color='red')
plt.xlabel("Taylor Hang getsu")
plt.ylabel("O Cha")
plt.title("Jwa Yeon Sang Su e wa Taylor jeaon gay")
plt.yscale("log")
plt.legend()
plt.grid(True)
plt.show()
