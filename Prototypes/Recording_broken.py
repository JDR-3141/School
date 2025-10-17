import sounddevice as sd
import numpy as np

# Set the duration and sampling frequency
duration = [1,2,3,4,5,10]  # seconds
fs = 44100  # sampling frequency

# Record audio
for d in duration:
    print("Recording...")
    myrecording = sd.rec(int(d * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()  # Wait until recording is finished
    print("Recording finished.")

    count_zero = myrecording.size - np.count_nonzero(myrecording)

    print(count_zero/myrecording.size)

