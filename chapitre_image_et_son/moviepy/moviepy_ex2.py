import moviepy.editor


piste_audio = moviepy.editor.AudioFileClip("/tmp/megamind.avi")
piste_audio = piste_audio.subclip(0, 4)
videos = [moviepy.editor.VideoFileClip(n, audio=False).subclip(0, 4)
          for n in ["/tmp/megamind.avi",
                    "/tmp/vtest.avi",
                    "/tmp/tree.avi"
                    ]
          ]
composition = [videos[0].resize((360, 132)).set_position((0, 0)),
               videos[1].resize((180, 132)).set_position((200, 80)),
               videos[2].resize((180, 132)).set_position((0, 400))]

cc = moviepy.video.compositing.CompositeVideoClip. \
    CompositeVideoClip(composition, size=(768, 576))
cc.audio = piste_audio
cc.write_videofile("/tmp/composition.mp4")
