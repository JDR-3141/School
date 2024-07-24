import cmath
from numpy import pi


def FFT (complex_vector):

    N = len (complex_vector)

    

    if N == 1:
        return complex_vector

    half_length = N // 2

    even = []
    odd = []
    for sample in range (0, len (complex_vector) - 1, 2):
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

def change_format(frequency_bins, sample_frequency):
    N = len(frequency_bins)
    frequency_bins = frequency_bins[:N//2-1]
    frequency_resolution = sample_frequency/N
    for i in range(len(frequency_bins)):
        frequency_bins[i] = [frequency_resolution*i, cmath.imag(frequency_bins[i]*2/N)]
    
    return frequency_bins



frequency_bins = FFT([0.0, 0.707, 1, 0.707, 0, -0.707, -1, -0.707])
print(frequency_bins)
print(change_format(list(frequency_bins[0]), 8))