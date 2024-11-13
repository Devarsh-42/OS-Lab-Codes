import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon, beta, gamma, t

n = 1000
rv1 = np.random.uniform(0, 1, n)  # Uniform distribution
rv2 = np.random.exponential(1, n)
rv2 = rv2 / np.max(rv2)
rv3 = np.random.beta(2, 5, n)
rv4 = np.random.gamma(2, 2, n)
rv4 = rv4 / np.max(rv4)
rv5 = t.rvs(df=3, size=n)

random_variables = [rv1, rv2, rv3, rv4, rv5]
distribution_names = ['Uniform', 'Exponential', 'Beta', 'Gamma', "Student's t"]

fig, axs = plt.subplots(2, 3, figsize=(15, 10))
for i, (rv, name) in enumerate(zip(random_variables, distribution_names)):
    ax = axs[i // 3, i % 3]  # Position in subplot grid
    ax.hist(rv, bins=30, alpha=0.7, density=True, label=f'RV{i + 1}')
    ax.set_title(f'{name} Distribution')
    ax.legend()

plt.tight_layout()
plt.show()

# Normalize the random variables
normalized_rvs = [(rv - np.mean(rv)) / np.std(rv) for rv in random_variables]
sum_of_rv = np.mean(normalized_rvs, axis=0)

plt.figure(figsize=(8, 6))
plt.hist(sum_of_rv, bins=30, alpha=0.7, density=True, label='Normalized Sum')
plt.title('Histogram of Normalized Sum of 5 RVs')
plt.legend()
plt.show()

fig, axs = plt.subplots(2, 3, figsize=(15, 10))  # 2x3 subplot grid
for i, (rv, name) in enumerate(zip(normalized_rvs, distribution_names)):
    ax = axs[i // 3, i % 3]
    ax.hist(rv, bins=30, alpha=0.7, density=True, label=f'RV{i + 1}')

    # Fit and overlay normal distribution
    mu, sigma = np.mean(rv), np.std(rv)  # Mean and standard deviation
    x = np.linspace(rv.min(), rv.max(), 100)  # Range for plotting the normal distribution
    ax.plot(x, norm.pdf(x, mu, sigma), color='red', label=f'Normal Fit')

    ax.set_title(f'{name} Distribution (Normalized)')
    ax.legend()

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(sum_of_rv, bins=30, alpha=0.7, density=True, label='Normalized Sum')

mu_sum, sigma_sum = np.mean(sum_of_rv), np.std(sum_of_rv)
x_sum = np.linspace(sum_of_rv.min(), sum_of_rv.max(), 100)
plt.plot(x_sum, norm.pdf(x_sum, mu_sum, sigma_sum), color='red', label='Normal Fit')

plt.title('Histogram of Normalized Sum of 5 RVs with Normal Fit')
plt.legend()
plt.show()