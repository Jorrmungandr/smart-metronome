import pyaudio
import wave

class Recorder:
  def __init__(self, chunk = 1024, rate = 44100):
    self.chunk = chunk
    self.rate = rate
    self.sample_format = pyaudio.paInt16  # 16 bits per sample
    self.channels = 2

  def record(self, seconds = 30, filename = 'output.wav'):
    print('Initializing recorder')
    p = pyaudio.PyAudio()

    stream = p.open(format=self.sample_format,
                    channels=self.channels,
                    rate=self.rate,
                    frames_per_buffer=self.chunk,
                    input=True)

    frames = []

    # Store data in chunks for 3 seconds
    for i in range(0, int(self.rate / self.chunk * seconds)):
        data = stream.read(self.chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()

    p.terminate()

    print('Finished recording')
    wf = wave.open(filename, 'wb')
    wf.setnchannels(self.channels)
    wf.setsampwidth(p.get_sample_size(self.sample_format))
    wf.setframerate(self.rate)
    wf.writeframes(b''.join(frames))
    wf.close()
