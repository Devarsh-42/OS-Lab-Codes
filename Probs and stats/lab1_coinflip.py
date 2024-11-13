import numpy as np
import matplotlib.pyplot as plt

n = int(input("Enter the number of trials: "))
k = int(input("Enter the number of coin flips in each trial: "))

S = np.zeros(n)
heads_counts = 0
tails_counts = 0

for i in range(n):
    flips = np.random.choice([-1, 1], size=k)
    S[i] = np.sum(flips)

    heads_counts += np.sum(flips == 1)
    tails_counts += np.sum(flips == -1)

heads_prob = np.mean(heads_counts / k)
tails_prob = np.mean(tails_counts / k)
i
print(f"Sum of outcomes (S): {S}")
print(f"Probability of heads: {heads_prob:.4f}")
print(f"Probability of tails: {tails_prob:.4f}")

plt.hist(S, bins=range(-k, k + 1), edgecolor='blue')
plt.title('Histogram of Coin Flip Experiment Sums')
plt.xlabel('Sum of Outcomes (S)')
plt.ylabel('Counts')
plt.grid(True)
plt.show()
