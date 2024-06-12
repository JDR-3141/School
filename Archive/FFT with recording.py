from scipy.fft import fft, fftfreq
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Sample rate
seconds = 3  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished

N = int(seconds * fs)  # Number of sample points
T = 1.0 / fs  # Sample spacing
x = np.linspace(0.0, N * T, N, endpoint=False)
y = myrecording
yf = fft(y)  # Compute the FFT
xf = fftfreq(N, T)[:N // 2]  # Frequency axis
plt.plot(xf, 2.0 / N * np.abs(yf[0:N // 2]))  # Plot the magnitude
plt.grid()
plt.show()

#This code shows the frequencies of the original sine waves 
# as spikes on the graph
#To apply this, I need to compute a transform every note 
# subdivision to find when notes start and stop

