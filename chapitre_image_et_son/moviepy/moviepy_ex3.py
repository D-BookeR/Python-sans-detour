import moviepy.editor


def modif_image(lire_image, tps_img):
    image = lire_image(tps_img)
    if 2 < tps_img < 3:
        return image[:, :, [2, 1, 0]]
    if 3 <= tps_img < 6:
        img = image.copy()
        base = int((tps_img - 3) * 100)
        img[0: base, 100: 100 + base, :] = [255, 0, 0]
        return img
    if 6 <= tps_img <= 9:
        img = image.copy()
        base = int(300 - (tps_img - 6) * 100)
        img[0: base, 100: 100 + base, :] = [255, 0, 0]
        return img
    return image


if __name__ == '__main__':
    video = moviepy.editor.VideoFileClip("/tmp/megamind.avi")
    video_modif = video.fl(modif_image)
    video_modif.write_videofile("/tmp/megamind_modif.mp4")
