import cmath
from numpy import pi
import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np
from copy import deepcopy
from tkinter import messagebox
from os import getcwd

import sys

sys.path.append(getcwd()+"\\Project\\Project Code")

from classes.Notes import Note
from modules.lilypond import convert


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


def next_power_of_two(x):
    return 1 if x == 0 else 2**(x - 1).bit_length()

def pad_to_power_of_two(complex_vector):
    N = len(complex_vector)
    next_pow2 = next_power_of_two(N)
    return np.pad(complex_vector, (0, next_pow2 - N), 'constant') if N < next_pow2 else complex_vector

def STFT(data, window_size, hop_size, sample_frequency, take):
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

    text = convert(take)
    return text
