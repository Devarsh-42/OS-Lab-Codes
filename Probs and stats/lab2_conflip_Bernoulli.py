import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
m = int(input("Enter the number of experiments (m): "))
n = int(input("Enter the number of coin flips in each experiment (n): "))
k = int(input("Enter the required number of successes (k): "))
X = np.random.choice([1, 0], size=(n, m))
S = np.sum(X, axis=0)
P = S / n
print(P)
plt.figure(figsize=(10, 6))
plt.plot(range(m), P, marker='o', linestyle='-', color='b', label='Simulated Probability')
plt.title('Probability of Successes in Each Experiment')
plt.xlabel('Experiment Number')
plt.ylabel('Probability of Successes')
plt.grid(True)
plt.legend()
plt.show()
average_prob = np.mean(S == k)
print(f"Average probability of getting exactly {k} "
      f"successes in {n} coin flips over {m} experiments: {average_prob}")
theoretical_prob = binom.pmf(k, n, 0.5)
print(f"Theoretical probability of getting exactly {k} successes in {n} coin flips: {theoretical_prob}")
ns = [10, 20, 30]
ks = [5, 10, 15]

print("\nTable: n, k, Simulated Average Probability, Theoretical Probability")
for n in ns:
    for k in ks:
        X = np.random.choice([1, 0], size=(n, m))
        S = np.sum(X, axis=0)
        average_prob = np.mean(S == k)
        theoretical_prob = binom.pmf(k, n, 0.5)
        print(f"{n}, {k}, {average_prob:.4f}, {theoretical_prob:.4f}")
