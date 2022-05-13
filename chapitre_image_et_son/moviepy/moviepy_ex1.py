import os
os.environ["IMAGEMAGICK_BINARY"] = \
    "/tmp/ImageMagick-7.1.0-portable-Q8-x64/convert.exe"
import moviepy.editor
import moviepy.video.tools.subtitles

video = moviepy.editor.VideoFileClip("/tmp/megamind.avi")
generateur = lambda texte: moviepy.video.VideoClip.TextClip(
        texte,
        font='Buxton-Sketch',
        fontsize=24,
        color='white',
        method='caption',
        size=video.size,
        align='South')
s_titre = moviepy.video.tools.subtitles.SubtitlesClip("/tmp/sous_titres.srt",
                                                      make_textclip=generateur)
video_avec_soustitres = moviepy.editor.CompositeVideoClip([video, s_titre])
video_avec_soustitres.write_videofile("/tmp/testsrt.mp4")
