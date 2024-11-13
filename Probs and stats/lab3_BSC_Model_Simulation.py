import numpy as np

# Input parameters
m = int(input("Enter the number of experiments (m): "))
n = int(input("Enter the number of bits in each experiment (n): "))

# Step 1: Generate transmitted bit sequence (X)
X = np.random.choice([1, 0], size=(n, m))
print("Transmitted bit sequence (X):\n", X)

# Step 2: Generate AWGN noise
noise = np.random.uniform(-0.7, 0.7, size=(n, m))
print("AWGN noise:\n", noise)

# Step 3: Simulate received signal (X + noise)
received_signal = X + noise
print("Received signal (X + noise):\n", received_signal)

# Step 4: Apply hard threshold to get received bits (Y)
Y = np.where(received_signal < 0.5, 0, 1)
print("Received bit sequence after thresholding (Y):\n", Y)

# Step 5: Calculate difference matrix D (X - Y)
D = X - Y
print("Difference Matrix (D):\n", D)

# Step 6: Calculate bit error probability Pe
Pe = np.sum(np.abs(D)) / (n * m)
print(f"Bit Error Probability (Pe): {Pe:.4f}")

# Step 10: Theoretical Probability Calculations
Px_1 = Px_0 = 0.5  # Assume uniform distribution for X
Py1_given_x1 = 1 - Pe
Py0_given_x1 = Pe
Py1_given_x0 = Pe
Py0_given_x0 = 1 - Pe
Py_1 = Px_1 * Py1_given_x1 + Px_0 * Py1_given_x0
Py_0 = Px_0 * Py0_given_x0 + Px_1 * Py0_given_x1
Px1_given_y1 = (Py1_given_x1 * Px_1) / Py_1
Px0_given_y1 = (Py1_given_x0 * Px_0) / Py_1
Px1_given_y0 = (Py0_given_x1 * Px_1) / Py_0
Px0_given_y0 = (Py0_given_x0 * Px_0) / Py_0

print("\nTheoretical Probabilities:")
print(f"P(Y=1|X=1): {Py1_given_x1:.4f}")
print(f"P(Y=0|X=1): {Py0_given_x1:.4f}")
print(f"P(Y=1|X=0): {Py1_given_x0:.4f}")
print(f"P(Y=0|X=0): {Py0_given_x0:.4f}")
print(f"P(Y=1): {Py_1:.4f}")
print(f"P(Y=0): {Py_0:.4f}")
print(f"P(X=1|Y=1): {Px1_given_y1:.4f}")
print(f"P(X=0|Y=1): {Px0_given_y1:.4f}")
print(f"P(X=1|Y=0): {Px1_given_y0:.4f}")
print(f"P(X=0|Y=0): {Px0_given_y0:.4f}")

# Step 11: Practical Probability Calculations
Px_1_practical = np.sum(X == 1) / (n * m)
Px_0_practical = np.sum(X == 0) / (n * m)
Py_1_practical = np.sum(Y == 1) / (n * m)
Py_0_practical = np.sum(Y == 0) / (n * m)
Py1_given_x1_practical = np.sum((X == 1) & (Y == 1)) / np.sum(X == 1)
Py0_given_x1_practical = np.sum((X == 1) & (Y == 0)) / np.sum(X == 1)
Py1_given_x0_practical = np.sum((X == 0) & (Y == 1)) / np.sum(X == 0)
Py0_given_x0_practical = np.sum((X == 0) & (Y == 0)) / np.sum(X == 0)
Px1_given_y1_practical = np.sum((X == 1) & (Y == 1)) / np.sum(Y == 1)
Px0_given_y1_practical = np.sum((X == 0) & (Y == 1)) / np.sum(Y == 1)
Px1_given_y0_practical = np.sum((X == 1) & (Y == 0)) / np.sum(Y == 0)
Px0_given_y0_practical = np.sum((X == 0) & (Y == 0)) / np.sum(Y == 0)

print("\nPractical Probabilities:")
print(f"P(Y=1|X=1): {Py1_given_x1_practical:.4f}")
print(f"P(Y=0|X=1): {Py0_given_x1_practical:.4f}")
print(f"P(Y=1|X=0): {Py1_given_x0_practical:.4f}")
print(f"P(Y=0|X=0): {Py0_given_x0_practical:.4f}")
print(f"P(Y=1): {Py_1_practical:.4f}")
print(f"P(Y=0): {Py_0_practical:.4f}")
print(f"P(X=1|Y=1): {Px1_given_y1_practical:.4f}")
print(f"P(X=0|Y=1): {Px0_given_y1_practical:.4f}")
print(f"P(X=1|Y=0): {Px1_given_y0_practical:.4f}")
print(f"P(X=0|Y=0): {Px0_given_y0_practical:.4f}")

# Step 12: Compare theoretical and practical probabilities
print("\nComparison of Theoretical and Practical Probabilities:")
comparison = {
    "P(Y=1|X=1)": (Py1_given_x1, Py1_given_x1_practical),
    "P(Y=0|X=1)": (Py0_given_x1, Py0_given_x1_practical),
    "P(Y=1|X=0)": (Py1_given_x0, Py1_given_x0_practical),
    "P(Y=0|X=0)": (Py0_given_x0, Py0_given_x0_practical),
    "P(Y=1)": (Py_1, Py_1_practical),
    "P(Y=0)": (Py_0, Py_0_practical),
    "P(X=1|Y=1)": (Px1_given_y1, Px1_given_y1_practical),
    "P(X=0|Y=1)": (Px0_given_y1, Px0_given_y1_practical),
    "P(X=1|Y=0)": (Px1_given_y0, Px1_given_y0_practical),
    "P(X=0|Y=0)": (Px0_given_y0, Px0_given_y0_practical),
}

for key, (theoretical, practical) in comparison.items():
    print(f"{key}: Theoretical = {theoretical:.4f}, Practical = {practical:.4f}")