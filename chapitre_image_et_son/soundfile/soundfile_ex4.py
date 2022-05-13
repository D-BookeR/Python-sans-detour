import sounddevice
import soundfile

duree = 3.5
freq_ech = 44100
nb_ech = int(duree * freq_ech)
enregis = sounddevice.rec(nb_ech, samplerate=freq_ech, channels=2)
sounddevice.wait()
soundfile.write('/tmp/mon_son.wav', enregis, freq_ech)
