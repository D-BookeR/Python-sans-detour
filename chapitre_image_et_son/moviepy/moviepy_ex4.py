import sys
import queue
import time
import sounddevice
import soundfile
import cv2
import moviepy.editor


def lire_son(son_in, _frames, _tps, status):
    if status:
        print(status, file=sys.stderr)
    file_son.put(son_in.copy())


if __name__ == '__main__':
    flux_entree = cv2.VideoCapture(0, cv2.CAP_ANY)
    if not flux_entree.isOpened():
        print("Le flux d'entrée ne peut être ouvert")
        sys.exit()
    resolution = (1280, 720)
    flux_entree.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
    flux_entree.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])
    resolution = (int(flux_entree.get(cv2.CAP_PROP_FRAME_WIDTH)),
                  int(flux_entree.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    fps = 5
    flux_sortie = cv2.VideoWriter('/tmp/output.avi', fourcc, fps, resolution)
    file_son = queue.Queue()
    if not flux_sortie.isOpened():
        print("Le flux de sortie ne peut être ouvert")
        flux_entree.release()
        sys.exit()
    with soundfile.SoundFile('/tmp/test.wav',
                             mode='w',
                             samplerate=44100,
                             channels=2,
                             subtype='PCM_16') as file:
        with sounddevice.InputStream(samplerate=44100,
                                     channels=2,
                                     callback=lire_son):
            tps_img = 1 / fps * 1e9
            tps_suivante = time.time_ns() + tps_img
            while True:
                x = file_son.get()
                file.write(x)
                if time.time_ns() > tps_suivante:
                    ret, img = flux_entree.read()
                    tps_suivante += tps_img
                    if not ret:
                        print("erreur ou fin de la lecture du flux")
                        break
                    flux_sortie.write(img)
                    cv2.imshow('Webcam', img)
                    if cv2.pollKey() == ord('q'):
                        break
            file.write(file_son.get())
    flux_entree.release()
    flux_sortie.release()
    cv2.destroyAllWindows()
    clip = moviepy.editor.VideoFileClip('/tmp/output.avi')
    audioclip = moviepy.editor.AudioFileClip("/tmp/test.wav")
    clip.audio = audioclip
    clip.write_videofile("c:/tmp/video.mp4")
    clip.close()
