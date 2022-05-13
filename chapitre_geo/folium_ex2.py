import io
import folium
import PIL.Image


carte = folium.Map([46.763, 2.425],
                   zoom_start=15,
                   zoom_control=False,
                   control_scale=True)
img_data = carte._to_png(2)
img = PIL.Image.open(io.BytesIO(img_data))
img.show()
img.save("/tmp/ma_carte.png")
