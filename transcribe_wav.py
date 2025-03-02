import os
# Set the backend via environment variable BEFORE importing torchaudio
os.environ["TORCHAUDIO_BACKEND"] = "soundfile"

import torch
import torchaudio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

# Define the directory path using a raw string to avoid escape sequence issues
wav_directory = r"F:\Voice_clone\wavs"
output_file = os.path.join(wav_directory, "list.txt")

wav_files_range = range(1, 26)
file_and_transcripts = []

model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h")

for i in wav_files_range:
    wav_file = os.path.join(wav_directory, f"{i}.wav")
    if os.path.exists(wav_file):
        try:
            waveform, sample_rate = torchaudio.load(wav_file)
            waveform = waveform.squeeze()
            # Resample the waveform to 16 kHz
            resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
            waveform = resampler(waveform)
            input_values = processor(waveform, return_tensors="pt", sampling_rate=16000).input_values
            logits = model(input_values).logits
            predicted_ids = torch.argmax(logits, dim=-1)
            transcript = processor.decode(predicted_ids[0])
        except Exception as e:
            print("Error processing file:", wav_file, e)
            continue
        file_and_transcripts.append(f"/content/TTS-TT2/wavs/{i}.wav|{transcript}")
    else:
        print("File not found:", wav_file)

with open(output_file, 'w') as f:
    for line in file_and_transcripts:
        f.write(f"{line}\n")

print(f"File '{output_file}' created successfully.")
