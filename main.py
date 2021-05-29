from audio.recorder import Recorder
from plot.wav import plot_wav

recorder = Recorder(chunk = 1024, rate = 44100)

recorder.record(seconds = 3, filename = 'output.wav')

plot_wav('output.wav')
