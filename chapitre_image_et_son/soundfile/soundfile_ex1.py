import sounddevice
import soundfile

mon_son, freq_ech = soundfile.read('/tmp/jvac.wav')
sounddevice.play(mon_son, freq_ech)
sounddevice.wait()
