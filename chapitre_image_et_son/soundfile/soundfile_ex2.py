import numpy
import sounddevice
import soundfile
import matplotlib.pyplot

mon_son, freq_ech = soundfile.read('/tmp/jvac.wav')
sounddevice.play(mon_son, freq_ech)
fig, ax = matplotlib.pyplot.subplots(nrows=1, ncols=1)
t = numpy.arange(0, mon_son.shape[0]) / freq_ech
ax.plot(t, mon_son[:, 0])
ax.plot(t, mon_son[:, 1])
ax.grid(True)
ax.set_xlabel('temps (s)')
ax.legend(['Voie gauche', 'Voie droite'])
matplotlib.pyplot.show()
