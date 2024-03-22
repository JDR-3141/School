import numpy as np

N = 600  # Number of sample points
T = 1.0 / 800.0  # Sample spacing
x = np.linspace(0.0, N * T, N, endpoint=False)
y = np.sin(50.0 * 2.0 * np.pi * x) + 0.5 * np.sin(80.0 * 2.0 * np.pi * x)

print([x,y])
