import io
import PIL.Image
import folium

l_carte = ["OpenStreetMap",
           "Stamen Terrain",
           "Stamen Toner",
           "Stamen Watercolor",
           "cartodb positron",
           "cartodb dark_matter"
           ]
largeur = 400
hauteur = 256
img_cartes = PIL.Image.new('RGB', (largeur * 3, hauteur * 2))
for idx, src_carte in enumerate(l_carte):
    carte = folium.Map([46.59, 2.48],
                       height=hauteur,
                       width=largeur,
                       tiles=src_carte,
                       control_scale=True,
                       zoom_start=10)
    img_data = carte._to_png(2)
    img = PIL.Image.open(io.BytesIO(img_data))
    idx_lig, idx_col = idx // 3, idx % 3
    origine = (idx_col * largeur, idx_lig * hauteur)
    img_cartes.paste(img, origine)
img_cartes.show()
