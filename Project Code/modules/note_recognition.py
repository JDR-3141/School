import cmath
from numpy import pi
import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np
from copy import deepcopy
from tkinter import messagebox
from os import getcwd

import sys

sys.path.append(getcwd()+"\\Project Code")

from classes.Notes import Note


global HPS_number
HPS_number = 1 # this seems to work for the guitar

CONCERT_PITCH = 440
ALL_NOTES = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]

def find_closest_note(pitch):


  i = int(np.round(np.log2(pitch/CONCERT_PITCH)*12))
  closest_note = ALL_NOTES[i%12] + str(4 + (i + 9) // 12)
  return closest_note


def FFT (complex_vector):
    if type(complex_vector) != np.ndarray:
            messagebox.showerror(title="Invalid FFT input", message="Unexpected input type received")
            return False
    else:
        complex_vector = pad_to_power_of_two(complex_vector)
        N = complex_vector.size


        if N == 1:
            return complex_vector

        half_length = N // 2

        even = []
        odd = []
        for sample in range (0, N, 2):
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

def quadratic_interpolation(magnitude_spectrum, bin_index):
    alpha = magnitude_spectrum[bin_index - 1]
    beta = magnitude_spectrum[bin_index]
    gamma = magnitude_spectrum[bin_index + 1]
    p = 0.5 * (alpha - gamma) / (alpha - 2 * beta + gamma)
    return bin_index + p

# def HPS(fft_output, sample_frequency, window_size):
#     frequency_resolution = sample_frequency/window_size
#     magnitude_spectrum = np.abs(fft_output[:fft_output.size//2])
#     for i in range(int(62/frequency_resolution)):
#         magnitude_spectrum[i] = 0

#     octaves = [50, 100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600]
#     for i in range(len(octaves)-1):
#         start = int(octaves[i]/frequency_resolution)
#         end = int(octaves[i+1]/frequency_resolution)
#         end = end if end < magnitude_spectrum.size else magnitude_spectrum.size
#         average_magnitude = ((np.linalg.norm(magnitude_spectrum[start:end], ord=2)**2)/(end-start))**0.5
#         for i in range(start, end):
#             magnitude_spectrum[i] = magnitude_spectrum[i] if magnitude_spectrum[i] > 0.2*average_magnitude else 0

#     #print(magnitude_spectrum)

#     interpolated_output = np.interp(np.arange(0, len(magnitude_spectrum), 1/HPS_number), np.arange(0, len(magnitude_spectrum)), magnitude_spectrum)
#     interpolated_output = interpolated_output / np.linalg.norm(interpolated_output, ord=2)
#     hps_spectrum = deepcopy(interpolated_output)

#     for i in range(HPS_number):
#         temp_hps_array = np.multiply(hps_spectrum[:int(np.ceil(len(interpolated_output)/(i+1)))], interpolated_output[::(i+1)])
#         if not any(temp_hps_array):
#             break
#         hps_spectrum = temp_hps_array
#         # decimated = fft_output[::i]
#         # hps_array[:len(decimated)] *= decimated

#     # hps_array_abs = np.abs(hps_array)
#     max_bin = np.argmax(hps_spectrum)

#         # Apply quadratic interpolation


#     max_frequency = max_bin * frequency_resolution / HPS_number
#     return max_frequency
    ##################################### WORK HERE NEXT!!!! 

def HPS(fft_output, sample_frequency, window_size):
    frequency_resolution = sample_frequency / window_size
    magnitude_spectrum = np.abs(fft_output[:fft_output.size // 2])
    
    # Zero out frequencies below 62 Hz
    for i in range(int(62 / frequency_resolution)):
        magnitude_spectrum[i] = 0
    
    hps_spectrum = deepcopy(magnitude_spectrum)
    
    # Apply HPS
    for i in range(2, HPS_number + 1):
        decimated_spectrum = magnitude_spectrum[::i]
        hps_spectrum[:len(decimated_spectrum)] *= decimated_spectrum
    
    max_bin = np.argmax(hps_spectrum)

    if max_bin > 0 and max_bin < len(hps_spectrum) - 1:
        max_bin = quadratic_interpolation(hps_spectrum, max_bin)
    max_frequency = max_bin * frequency_resolution
    
    max_frequency = max_frequency if max_frequency > 62 else 0
    return max_frequency


# def change_format(frequency_bins, sample_frequency):
#     N = frequency_bins.size
#     frequency_bins = frequency_bins[:N//2]
#     frequency_resolution = sample_frequency/N
#     frequency_bins_list = [frequency_resolution*i for i in range(N//2)]
#     f = lambda x: round(abs(x)*2/N, 3)
#     vf = np.vectorize(f)
#     frequency_bins_magnitude  = vf(frequency_bins)
#     return frequency_bins_list, frequency_bins_magnitude # outputs a list of frequencies and a numpy array of magnitudes


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
    time = []
    time_period = 1/sample_frequency
    for start in range(0, data.size - window_size, hop_size):
        segment = data[start:start + window_size]
        windowed_segment = np.multiply(segment, window)
        frequency_bins = FFT(windowed_segment)
        if type(frequency_bins) != np.ndarray:
            return 0
        #formatted_bins, magnitudes = change_format(frequency_bins, sample_frequency)
        frequency_found = HPS(frequency_bins, sample_frequency, window_size)
        stft_result.append(frequency_found)
        time.append(start*time_period)

    for i in range(len(stft_result)):
        if i > 0 and i < len(stft_result) - 1:
            if abs(stft_result[i] - stft_result[i-1]) > 10 and abs(stft_result[i] - stft_result[i+1]) > 10:
                stft_result[i] = 0

    if abs(stft_result[0] - stft_result[1]) > 10:
        stft_result[0] = 0

    if abs(stft_result[-1] - stft_result[-2]) > 10:
        stft_result[-1] = 0

    for i in range(len(stft_result)):
        if stft_result[i] != 0:
            stft_result[i] = find_closest_note(stft_result[i])

    filler_note = Note(None, None)
    current_note = filler_note

    for i in range(len(stft_result)):
        if stft_result[i] != 0:
            if current_note.get_pitch() != stft_result[i]:
                Note(time[i], stft_result[i])
                current_note.set_end(time[i])
                current_note = Note.notes[-1]
        else:
            current_note.set_end(time[i])
            current_note = filler_note

    # for note in Note.notes:
    #     print(note)


    #return time, stft_result

# samplerate, data = wavfile.read('test_audio.wav')
# samplerate, data1 = wavfile.read('test_audio1.wav')
# result_lt = np.concatenate((data, data1))
# wavfile.write('test_audio2.wav', samplerate, result_lt)
samplerate, result_lt = wavfile.read('test.wav')
STFT(result_lt, 1024, 512, samplerate)
#result_lt = result_lt / np.max(np.abs(result_lt))
########x, frequency_bins = STFT(result_lt, 1024, 512, samplerate)
########x = np.array(x)
########frequency_bins = np.array(frequency_bins)


########plt.scatter(x, frequency_bins)

########plt.yscale('log')

########plt.ylim(10, 4500)

########plt.show()
# plt.figure(figsize=(10, 6))
# for i, frame in enumerate(frequency_bins):
#     plt.plot([f[0] for f in frame], [f[1] for f in frame], label=f'Frame {i}')
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Magnitude')
# plt.title('STFT Magnitude Spectrum')
# plt.legend()
# plt.show()