# Voice Cloning Experiment with Tacotron 2 & FakeYou 🎤🤖

Welcome to my voice cloning experiment! In this project, I explored cloning a unique voice by combining the power of Tacotron 2 and the FakeYou colab notebook. The entire process involved multiple steps—from recording the audio to training the model.

## Overview 🚀
The goal of this project was to clone a voice using a custom dataset of 25 recorded audio samples. The process included:

- Recording Audio 🎙️: Captured 25 sample audio files.
- Transcription 📝: Generated transcriptions for each audio file.
- Preprocessing ✂️: Trimmed, normalized, and cleaned up the audio.
- Metadata Editing 🏷️: Updated file metadata to ensure consistency.
- Training with FakeYou Colab Notebook 💻: Used the prepared dataset to train a voice cloning model.


## Project Workflow 📋
1. Audio Recording 🎙️:

- Recorded 25 sample audio files and stored them in a designated directory.
2. Transcription 📝:

- Created transcriptions for each audio file using an automated transcription pipeline (e.g., Wav2Vec2).
3. Audio Preprocessing ✂️:

- Preprocessed the audio files by trimming silence and normalizing the volume to ensure consistency for training.
4. Metadata Editing 🏷️:

- Updated each audio file’s metadata (like title and track number) using a Python script with the taglib library.
5. Voice Cloning Training 💻:

- Imported the processed data into the FakeYou colab notebook to train the voice cloning model based on the Tacotron 2 architecture.


## FakeYou Architecture Explained 🏗️
FakeYou is a state-of-the-art voice cloning system that leverages deep learning. Here’s a quick breakdown of its core components:

- **Text-to-Spectrogram Module (Tacotron 2) 🎶:** Tacotron 2 converts input text into a mel-spectrogram, capturing the prosody and intonation of the speaker.

- **Neural Vocoder (e.g., WaveGlow) 🔊:** The vocoder transforms the mel-spectrogram into a raw audio waveform, resulting in natural-sounding synthesized speech.

- **Speaker Embedding & Fine-Tuning 🧠:** The system uses speaker embeddings to capture and reproduce the unique characteristics of the target voice. Fine-tuning this component is key for achieving a realistic voice clone.

- **Training Pipeline 🏃:** The overall pipeline involves data loading, preprocessing, model training, and periodic checkpointing to ensure progress is saved. The FakeYou colab notebook integrates these components into a streamlined training process.

