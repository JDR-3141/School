import librosa
import numpy as np

def extract_piano_notes(audio_file):
    # Load the audio file
    y, sr = librosa.load(audio_file)

    # Compute the Short-Time Fourier Transform (STFT)
    D = librosa.stft(y)

    # Convert STFT to frequencies
    frequencies = np.abs(D)

    # Assume piano notes: C3 to C7 (adjust as needed)
    note_names = ["C3", "C#3", "D3", ..., "B6", "C7"]

    # Initialize an empty list to store notes
    piano_notes = []

    # Threshold for detecting notes (adjust as needed)
    threshold = 0.1

    for i, freq_row in enumerate(frequencies):
        for j, freq_val in enumerate(freq_row):
            if freq_val > threshold:
                # Map frequency index to note name
                note_index = j % len(note_names)
                note = note_names[note_index]

                # Calculate start time (in seconds)
                start_time = librosa.frames_to_time(i, sr=sr)

                # Append note info to our list
                piano_notes.append({"note": note, "start_time": start_time})

    return piano_notes

if __name__ == "__main__":
    audio_file_path = "output.wav"
    piano_notes = extract_piano_notes(audio_file_path)

    # Print the notes (you can write them to a file if needed)
    for note_info in piano_notes:
        print(f"Note: {note_info['note']} | Start Time: {note_info['start_time']:.2f} seconds")

