#########################################################################################################
# Imports

import sounddevice as sd 
from scipy.io.wavfile import write

#########################################################################################################


fs = 44100  # Sample rate
seconds = 10  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
print(myrecording) # Print the array to check format
write('output.wav', fs, myrecording) 

class Recording:

    def __init__(self, fs, seconds, user, song, take):
        pass