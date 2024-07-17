from scipy.io.wavfile import write, read
import numpy as np
import sounddevice as sd # Learnt to use this module to record - possible use stream in future?

samplerate = 44100  # Sample rate
seconds = 10 # Duration of recording

data = sd.rec(int(seconds * samplerate), samplerate=samplerate, channels=1)
sd.wait()  # Wait until recording is finished
#t = np.linspace(0., 1., samplerate)
#amplitude = np.iinfo(np.int16).max
#data = amplitude * np.sin(2. * np.pi * samplerate * t)
write("example.wav", samplerate, data.astype(np.float32))

samplerate, data = read("example.wav")

import matplotlib.pyplot as plt

# Assuming you have an audio array called 'data'
# Compute the FFT
fft_result = np.fft.fft(data)

# Get the corresponding frequencies
n = len(data)
freq = np.fft.fftfreq(n, d=1/samplerate)

# Plot the one-sided spectrum
plt.figure(figsize=(10, 6))
plt.plot(freq[:n//2], np.abs(fft_result[:n//2]), 'b')
plt.xlabel('Frequency (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
plt.xscale("log")
plt.xlim(32, 4000)
plt.title('Frequency Spectrum')
plt.grid(True)
plt.show()