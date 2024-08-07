import cmath
from numpy import pi
import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np

global HPS_number
HPS_number = 4

def FFT (complex_vector):
    complex_vector = pad_to_power_of_two(complex_vector)
    N = len (complex_vector)

    

    if N == 1:
        return complex_vector

    half_length = N // 2

    even = []
    odd = []
    for sample in range (0, N-1, 2):
        even.append( complex_vector [sample])
        odd.append( complex_vector [sample + 1])

    even_result = FFT (even)
    odd_result = FFT (odd)

    frequency_bins = [0] * N

    for i in range(half_length):

        complex_exponential = cmath.rect(1.0, -2*pi*i/N)*odd_result[i]
        frequency_bins[i] = even_result[i]+complex_exponential
        frequency_bins[i+half_length] = even_result[i]-complex_exponential

    return frequency_bins

# def HPS(frequency_bins):
#     for i in range(HPS_number)

def change_format(frequency_bins, sample_frequency):
    N = len(frequency_bins)
    frequency_bins = frequency_bins[:N//2]
    frequency_resolution = sample_frequency/N
    for i in range(N//2):
        frequency_bins[i] = [frequency_resolution*i, round(abs(frequency_bins[i])*2/N, 3)]
    
    return frequency_bins


def next_power_of_two(x):
    return 1 if x == 0 else 2**(x - 1).bit_length()

def pad_to_power_of_two(complex_vector):
    N = len(complex_vector)
    next_pow2 = next_power_of_two(N)
    return complex_vector + [0] * (next_pow2 - N)

def apply_window(segment, window):
    return [s * w for s, w in zip(segment, window)]


def STFT(data, window_size, hop_size, sample_frequency):
    window = np.hanning(window_size)
    stft_result = []
    for start in range(0, len(data) - window_size, hop_size):
        segment = data[start:start + window_size]
        windowed_segment = apply_window(segment, window)
        frequency_bins = FFT(windowed_segment)
        formatted_bins = change_format(frequency_bins, sample_frequency)
        stft_result.append(formatted_bins)
    return stft_result

samplerate, data = wavfile.read('test_audio.wav')
samplerate, data1 = wavfile.read('test_audio1.wav')
result_lt = np.array(list(data) + list(data1))
wavfile.write('test_audio2.wav', samplerate, result_lt)
result_lt = result_lt / np.max(np.abs(result_lt))
frequency_bins = STFT(list(result_lt), 1024, 512, samplerate)

plt.figure(figsize=(10, 6))
for i, frame in enumerate(frequency_bins):
    plt.plot([f[0] for f in frame], [f[1] for f in frame], label=f'Frame {i}')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('STFT Magnitude Spectrum')
plt.legend()
plt.show()