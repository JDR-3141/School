# https://docs.scipy.org/doc/scipy/tutorial/fft.html
from scipy.fft import fft, fftfreq
import numpy as np
import matplotlib.pyplot as plt

N = 600  # Number of sample points
T = 1.0 / 800.0  # Sample spacing
x = np.linspace(0.0, N * T, N, endpoint=False)
y = np.sin(50.0 * 2.0 * np.pi * x) + 0.5 * np.sin(80.0 * 2.0 * np.pi * x) + np.sin(440.0 * 2.0 * np.pi * x)
yf = fft(y)  # Compute the FFT
xf = fftfreq(N, T)[:N // 2]  # Frequency axis
plt.plot(xf, 2.0 / N * np.abs(yf[0:N // 2]))  # Plot the magnitude
plt.grid()
plt.show()

#This code shows the frequencies of the original sine waves 
# as spikes on the graph
#To apply this, I need to compute a transform every note 
# subdivision to find when notes start and stop
