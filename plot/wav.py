import wave
import matplotlib.pyplot as plt
import numpy as np

def plot_wav(filename = 'output.wav'):
  spf = wave.open(filename, 'r')

  signal = spf.readframes(-1)
  signal = np.frombuffer(signal, np.int16)

  plt.figure(1)
  plt.title("Signal Wave")
  plt.plot(signal)
  plt.show()