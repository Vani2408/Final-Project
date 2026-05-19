import numpy as np
import wave

sample_rate = 44100
duration = 0.15  # short & crisp
frequency = 900  # high pitch = coin feel

t = np.linspace(0, duration, int(sample_rate * duration))

# coin sound with fade-out
wave_data = (np.sin(2 * np.pi * frequency * t) * np.exp(-8*t) * 32767).astype(np.int16)

with wave.open("coin.wav", "w") as f:
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(sample_rate)
    f.writeframes(wave_data.tobytes())