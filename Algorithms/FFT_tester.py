import numpy as np

# Test inputs for an FFT algorithm at 1 Hz
sampling_frequencies = [100]  # in Hz

# Calculate the corresponding number of samples for 1 second
duration = 1  # seconds
num_samples = [int(freq * duration) for freq in sampling_frequencies]

# Create the test inputs (sine waves at 1 Hz)
test_inputs = []
for freq, samples in zip(sampling_frequencies, num_samples):
    time_values = np.linspace(0, duration, samples)
    sine_wave = np.sin(2 * np.pi * 1 * time_values)  # 1 Hz sine wave
    test_inputs.append(sine_wave.tolist())

print(test_inputs)
