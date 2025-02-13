import sounddevice as sd
import numpy as np

samplerate = 16000
duration = 5  # Record for 5 seconds

print("Recording...")
audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
sd.wait()  # Wait for recording to finish
print("Playing back...")
sd.play(audio, samplerate)
sd.wait()  # Wait for playback to finish