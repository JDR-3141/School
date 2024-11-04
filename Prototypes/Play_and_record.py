import numpy as np
import sounddevice as sd
import time
import threading

def record_with_toggle_sinewave(beat_time, duration, sample_rate=44100):
    def generate_sinewave(frequency, duration, sample_rate):
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        return 0.5 * np.sin(2 * np.pi * frequency * t)

    def toggle_sinewave():
        nonlocal playing
        while time.time() - start_time < duration:
            playing = not playing
            if playing:
                sd.play(sine_wave, samplerate=sample_rate, loop=True)
            else:
                sd.stop()
            time.sleep(beat_time)

    # Generate the 30Hz sine wave
    sine_wave = generate_sinewave(3000, beat_time, sample_rate)

    # Initialize recording
    recording = np.empty((0, 1), dtype=np.float32)
    playing = False
    start_time = time.time()

    # Start the toggle thread
    toggle_thread = threading.Thread(target=toggle_sinewave)
    toggle_thread.start()

    # Record audio
    with sd.InputStream(samplerate=sample_rate, channels=1, dtype='float32') as stream:
        while time.time() - start_time < duration:
            frames, _ = stream.read(int(sample_rate * beat_time))
            recording = np.append(recording, frames, axis=0)

    # Stop playback if still playing
    if playing:
        sd.stop()

    # Wait for the toggle thread to finish
    toggle_thread.join()

    return recording

# Example usage
beat_time = 0.5  # Toggle every 1 second
duration = 5.0   # Record for 5 seconds
recorded_audio = record_with_toggle_sinewave(beat_time, duration)
