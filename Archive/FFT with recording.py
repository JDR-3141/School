# from scipy.fft import fft, fftfreq
# import numpy as np
# import matplotlib.pyplot as plt
# import sounddevice as sd
# from scipy.io.wavfile import write

# fs = 44100  # Sample rate
# seconds = 10  # Duration of recording

# myRecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
# sd.wait()  # Wait until recording is finished

# N = int(seconds * fs)  # Number of sample points
# T = 1.0 / fs  # Sample spacing
# x = np.linspace(0.0, N * T, N, endpoint=False)
# y = myrecording
# yf = fft(y)  # Compute the FFT
# xf = fftfreq(N, T)[:N // 2]  # Frequency axis
# plt.plot(xf, 2.0 / N * np.abs(yf[0:N // 2]))  # Plot the magnitude
# plt.grid()
# plt.show()
import sounddevice as sd
import scipy.io.wavfile
import time

SAMPLE_FREQ = 44100 # Sampling frequency of the recording
SAMPLE_DUR = 2  # Duration of the recoding

print("Grab your guitar!")
time.sleep(1) # Gives you a second to grab your guitar ;)

myRecording = sd.rec(SAMPLE_DUR * SAMPLE_FREQ, samplerate=SAMPLE_FREQ, channels=1,dtype='float64')
print("Recording audio")
sd.wait()

sd.play(myRecording, SAMPLE_FREQ)
print("Playing audio")
sd.wait()

scipy.io.wavfile.write('example1.wav', SAMPLE_FREQ, myRecording)

import scipy.io.wavfile
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft

fs, myRecording = scipy.io.wavfile.read("example1.wav")
sampleDur = len(myRecording)/fs
timeX = np.arange(0, fs/2, fs/len(myRecording))
absFreqSpectrum = abs(fft(myRecording))
print(absFreqSpectrum)

plt.plot(timeX, absFreqSpectrum[:len(myRecording)//2])
plt.ylabel('|X(n)|')
plt.xlabel('frequency[Hz]')
plt.show()

#This code shows the frequencies of the original sine waves 
# as spikes on the graph
#To apply this, I need to compute a transform every note 
# subdivision to find when notes start and stop

