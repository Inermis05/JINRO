import numpy as np
import matplotlib.pyplot as plt

#e^(-x^2)
def f(x):
    return np.exp(-x**2)

# 사다리리
def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    return h * result

# 심프슨1/3
def simpsons_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Simpson's rule requires even n")
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n):
        coeff = 4 if i % 2 != 0 else 2
        result += coeff * f(a + i * h)
    return h * result / 3

# 적분 구간ㅊ 나누기
a, b = 0, 1
n_values = list(range(2, 51, 2))
trapezoid_results = [trapezoidal_rule(f, a, b, n) for n in n_values]
simpson_results = [simpsons_rule(f, a, b, n) for n in n_values]

from math import erf, sqrt
true_val = 0.5 * sqrt(np.pi) * erf(1)


trap_errors = [abs(true_val - val) for val in trapezoid_results]
simp_errors = [abs(true_val - val) for val in simpson_results]


plt.figure(figsize=(10, 5))
plt.plot(n_values, trap_errors, marker='o', label="SaDaRi O Cha")
plt.plot(n_values, simp_errors, marker='s', label="Sim O Cha")
plt.yscale("log")
plt.xlabel("9gan Su")
plt.ylabel("ZZIN O Cha")
plt.title("Sadarino Capuchino vs SimSimSimSimSimSimSimSimSim pson")
plt.legend()
plt.grid(True)
plt.show()
