import numpy as np
import matplotlib.pyplot as plt
import math


# Function to calculate binomial coefficient C(n, k)
def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


# Function to calculate binomial PMF
def binomial_pmf(n, p, k):
    return binomial_coefficient(n, k) * (p ** k) * ((1 - p) ** (n - k))


# Generate custom PMF for varying p and n
def plot_custom_binomial_pmf():
    p_values = np.arange(0.1, 1.0, 0.4)
    n_values = range(2, 11)

    fig, axs = plt.subplots(len(p_values), len(n_values), figsize=(18, 10))
    fig.suptitle('Custom Binomial PMF')

    for i, p in enumerate(p_values):
        for j, n in enumerate(n_values):
            k_values = range(n + 1)
            pmf_values = [binomial_pmf(n, p, k) for k in k_values]

            ax = axs[i, j]
            ax.bar(k_values, pmf_values)
            ax.set_title(f'p = {p}, n = {n}')
            ax.set_xlabel('k')
            ax.set_ylabel('PMF')

    plt.tight_layout()
    plt.show()


# Generate and plot histograms using numpy's built-in binomial function
def plot_numpy_binomial_hist():
    p_values = np.arange(0.1, 1.0, 0.4)
    n_values = range(2, 11)

    fig, axs = plt.subplots(len(p_values), len(n_values), figsize=(18, 10))
    fig.suptitle('Numpy Binomial Histograms')

    for i, p in enumerate(p_values):
        for j, n in enumerate(n_values):
            samples = np.random.binomial(n, p, size=1000)

            ax = axs[i, j]
            ax.hist(samples, bins=np.arange(n + 2) - 0.5, density=True, rwidth=0.8)
            ax.set_title(f'p = {p}, n = {n}')
            ax.set_xlabel('k')
            ax.set_ylabel('Frequency')

    plt.tight_layout()
    plt.show()


# Plot custom binomial PMF
plot_custom_binomial_pmf()

# Plot numpy-generated binomial histograms
plot_numpy_binomial_hist()
