import matplotlib.pyplot as plt

def babylonian_sqrt(S, initial_guess=1.0, tolerance=1e-10, max_iter=100):
    guesses = [initial_guess]
    for _ in range(max_iter):
        next_guess = 0.5 * (guesses[-1] + S / guesses[-1])
        guesses.append(next_guess)
        if abs(next_guess - guesses[-2]) < tolerance:
            break
    return guesses

S = 2
true_val = S**0.5
guesses = babylonian_sqrt(S)

errors = [abs(guess - true_val) for guess in guesses]

plt.figure(figsize=(10, 5))
plt.plot(range(len(guesses)), guesses, marker='o', label="Babi GunSa")
plt.axhline(y=true_val, color='gray', linestyle='--', label="ZZIN root2")
plt.xlabel("repeat")
plt.ylabel("Gun Sa Gap")
plt.title("root2 Babi")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(range(len(errors)), errors, marker='o', color='red', label="ZZIN O Cha")
plt.yscale("log")
plt.xlabel("repeat")
plt.ylabel("O cha")
plt.title("root2 Babi")
plt.legend()
plt.grid(True)
plt.show()
