import numpy as np
import matplotlib.pyplot as plt
# Exp 6
np.random.seed(42)
W = np.random.normal(0, 1, 2000)
time_index = np.arange(2000)

global_mean = np.mean(W)
global_variance = np.var(W)

chunk_size = 100
num_chunks = len(W) // chunk_size
chunk_means = []
chunk_variances = []

for i in range(num_chunks):
    chunk = W[i * chunk_size:(i + 1) * chunk_size]
    chunk_means.append(np.mean(chunk))
    chunk_variances.append(np.var(chunk))

fig, axs = plt.subplots(2, 1, figsize=(10, 6))

axs[0].plot(chunk_means, label='Chunk Means')
axs[0].hlines(global_mean, 0, num_chunks-1, colors='r', label='Global Mean', linestyles='dashed')
axs[0].set_title("Comparison of Chunk Means with Global Mean")
axs[0].set_xlabel("Chunk Index")
axs[0].set_ylabel("Mean")
axs[0].legend()

axs[1].plot(chunk_variances, label='Chunk Variances')
axs[1].hlines(global_variance, 0, num_chunks-1, colors='r', label='Global Variance', linestyles='dashed')
axs[1].set_title("Comparison of Chunk Variances with Global Variance")
axs[1].set_xlabel("Chunk Index")
axs[1].set_ylabel("Variance")
axs[1].legend()

plt.tight_layout()
plt.show()

fig, axs = plt.subplots(2, 1, figsize=(10, 6))

axs[0].acorr(W, maxlags=50)
axs[0].set_title("Autocorrelation Function (ACF) of White Noise")

axs[1].psd(W, NFFT=256, Fs=1)
axs[1].set_title("Power Spectral Density (PSD) of White Noise")

plt.tight_layout()
plt.show()

F = (W[:-2] + W[1:-1] + W[2:]) / 3

plt.figure(figsize=(10, 4))
plt.plot(F, label="Filtered Data (F)")
plt.title("Filtered White Noise Process (3-tap Moving Average)")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.legend()
plt.show()

fig, axs = plt.subplots(2, 1, figsize=(10, 6))

axs[0].acorr(F, maxlags=50)
axs[0].set_title("Autocorrelation Function (ACF) of Filtered Process")

axs[1].psd(F, NFFT=256, Fs=1)
axs[1].set_title("Power Spectral Density (PSD) of Filtered Process")

plt.tight_layout()
plt.show()