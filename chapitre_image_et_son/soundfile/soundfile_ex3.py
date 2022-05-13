import numpy
import sounddevice
import soundfile

mon_son, freq_ech = soundfile.read('/tmp/jvac.wav')
mon_son[:, 1] = mon_son[:, 0]
sounddevice.play(mon_son, freq_ech)
sounddevice.wait()
