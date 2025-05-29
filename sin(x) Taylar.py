import numpy as np
import matplotlib.pyplot as plt
import math

def taylor_sin(x, n_terms):
    return sum(((-1)**k * x**(2*k + 1)) / math.factorial(2*k + 1) for k in range(n_terms))

x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 500)
true_sin = np.sin(x_vals)

approximations = {
    "3 terms": [taylor_sin(x, 3) for x in x_vals],
    "5 terms": [taylor_sin(x, 5) for x in x_vals],
    "10 terms": [taylor_sin(x, 10) for x in x_vals],
}

plt.figure(figsize=(10, 6))
plt.plot(x_vals, true_sin, label="ZZIN sin(x)", color="black", linestyle="--")
for label, approx_vals in approximations.items():
    plt.plot(x_vals, approx_vals, label=f"Taylor Gun Sa ({label})")

plt.title("sin(x) Taylor jeaon gay")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend()
plt.grid(True)
plt.show()
