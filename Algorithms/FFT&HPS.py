import cmath
from numpy import pi
import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np

global HPS_number
HPS_number = 4

def FFT (complex_vector):
    complex_vector = pad_to_power_of_two(complex_vector)
    N = complex_vector.size

    

    if N == 1:
        return complex_vector

    half_length = N // 2

    even = []
    odd = []
    for sample in range (0, N-1, 2):
        even.append( complex_vector [sample])
        odd.append( complex_vector [sample + 1])

    even = np.array(even)
    odd = np.array(odd)

    even_result = FFT (even)
    odd_result = FFT (odd)

    frequency_bins = [0] * N
    frequency_bins = np.array(frequency_bins, dtype="complex_")

    for i in range(half_length):

        complex_exponential = cmath.rect(1.0, -2*pi*i/N)*odd_result[i]
        frequency_bins[i] = even_result[i]+complex_exponential
        frequency_bins[i+half_length] = even_result[i]-complex_exponential

    return frequency_bins

def HPS(fft_output):
    interpolated_output = np.interp(np.arange(0, len(fft_output), 1/HPS_number), np.arange(0, len(fft_output)), fft_output)
    print(interpolated_output)
    return interpolated_output
    ################################################################################### WORK HERE NEXT!!!! 

def change_format(frequency_bins, sample_frequency):
    N = frequency_bins.size
    frequency_bins = frequency_bins[:N//2]
    frequency_resolution = sample_frequency/N
    frequency_bins_list = [frequency_resolution*i for i in range(N//2)]
    f = lambda x: round(abs(x)*2/N, 3)
    vf = np.vectorize(f)
    frequency_bins_magnitude  = vf(frequency_bins)
    return frequency_bins_list, frequency_bins_magnitude # outputs a list of frequencies and a numpy array of magnitudes


def next_power_of_two(x):
    return 1 if x == 0 else 2**(x - 1).bit_length()

def pad_to_power_of_two(complex_vector):
    N = len(complex_vector)
    next_pow2 = next_power_of_two(N)
    return np.pad(complex_vector, (0, next_pow2 - N), 'constant') if N < next_pow2 else complex_vector

# def apply_window(segment, window):
#     return [s * w for s, w in zip(segment, window)]


def STFT(data, window_size, hop_size, sample_frequency):
    window = np.hanning(window_size)
    stft_result = []
    for start in range(0, data.size - window_size, hop_size):
        segment = data[start:start + window_size]
        windowed_segment = np.multiply(segment, window)
        frequency_bins = FFT(windowed_segment)
        formatted_bins, magnitudes = change_format(frequency_bins, sample_frequency)
        magnitudes = HPS(magnitudes)
        stft_result.append([formatted_bins, list(magnitudes)])
    return stft_result

samplerate, data = wavfile.read('test_audio.wav')
samplerate, data1 = wavfile.read('test_audio1.wav')
result_lt = np.concatenate((data, data1))
wavfile.write('test_audio2.wav', samplerate, result_lt)
#result_lt = result_lt / np.max(np.abs(result_lt))
frequency_bins = STFT(result_lt, 1024, 512, samplerate)
print(frequency_bins[0])
plt.figure(figsize=(10, 6))
for i, frame in enumerate(frequency_bins):
    plt.plot([f[0] for f in frame], [f[1] for f in frame], label=f'Frame {i}')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('STFT Magnitude Spectrum')
plt.legend()
plt.show()