import numpy as np

# Define system parameters
m = 1.0  # Mass of each oscillator (kg)
K1 = 10.0  # Spring constant for adjacent connections (N/m)
K2 = 5.0   # Spring constant for next-nearest connections (N/m)
K3 = 2.0   # Spring constant for opposite connections (N/m)
# Number of oscillators
N = 6

# Initialize the stiffness matrix K as a zero matrix
K = np.zeros((N, N))

# Define connections based on circular symmetry
# Each mass is connected to:
# - Its immediate neighbors with spring constant K1
# - Its next-nearest neighbors with spring constant K2
# - The opposite mass with spring constant K3

for i in range(N):
    # Immediate neighbors (K1)
    j1 = (i + 1) % N
    j2 = (i - 1) % N
    K[i, j1] -= K1
    K[i, j2] -= K1
    K[i, i] += K1 + K1  # Each K1 connection adds to the diagonal
    
    # Next-nearest neighbors (K2)
    j3 = (i + 2) % N
    j4 = (i - 2) % N
    K[i, j3] -= K2
    K[i, j4] -= K2
    K[i, i] += K2 + K2  # Each K2 connection adds to the diagonal
    
    # Opposite mass (K3)
    j5 = (i + 3) % N
    K[i, j5] -= K3
    K[i, i] += K3  # Each K3 connection adds to the diagonal

# Display the stiffness matrix K
print("Stiffness Matrix K:")
print(K)

# Compute eigenvalues and eigenvectors of the stiffness matrix K
eigenvalues, eigenvectors = np.linalg.eigh(K)

# Display the eigenvalues
print("\nEigenvalues (ω^2):")
for idx, val in enumerate(eigenvalues):
    print(f"Mode {idx + 1}: {val:.2f} rad^2/s^2")

# Display the eigenvectors
print("\nEigenvectors (Normal Modes):")
for idx, vec in enumerate(eigenvectors.T):
    print(f"Mode {idx + 1}: {vec}")
