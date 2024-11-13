import numpy as np
import matplotlib.pyplot as plt

# generate 10^6 arnd integers no. [-10,10] having Unfiorm prob. dist.

np.random.seed(42)

random_integers = np.random.randint(-10, 11, size=10**6)

plt.figure(figsize=(10, 6))
plt.hist(random_integers, bins=21, edgecolor='black', alpha=0.7)
plt.title('Histogram of 1,000,000 Random Integers in the Range [-10, 10]')
plt.xlabel('Integer Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# generate 10^6 arnd integers no. [-10,10] having Normal prob. dist.
mu, sigma = 0, 5
normal_floats = np.random.normal(mu, sigma, 10**6)
plt.figure(figsize=(10, 6))

normal_integers = np.round(normal_floats).astype(int)
normal_integers = np.clip(normal_integers, -10,10)

mean = np.mean(normal_integers)
variance = np.var(normal_integers)

print(f"Mean : {mean}, Variance: {variance}")

plt.hist(normal_integers, bins=21, edgecolor='black', alpha=0.7)
plt.title('Histogram of 1,000,000 Random Integers in the Range [-10, 10] with Normal Distribution')
plt.xlabel('Integer Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

