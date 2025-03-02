import os
import librosa
import soundfile as sf
"""
For Preprocessing the audio files:
Trimming the silence parts of the audio from the start to the end
Normalizes it to adjust the amplitude, ensuring consistent volumn levels across all files
Save a new copy of the preproessed files
"""

input_path = r"F:\Voice_clone\wavs"
output_path = r"F:\Voice_clone\output"

if not os.path.exists(output_path):
    os.makedirs(output_path)

for filename in os.listdir(input_path):
    filepath = os.path.join(input_path, filename)
    try:
        y, sr = librosa.load(filepath, sr=22050)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        continue

    trimmed_audio, _ = librosa.effects.trim(y, top_db=20)
    normalized_audio = librosa.util.normalize(trimmed_audio)
    output_filepath = os.path.join(output_path, filename)
    sf.write(output_filepath, normalized_audio, sr, subtype='PCM_16')

print("All .wav files have been preprocessed and saved to the output folder.")
