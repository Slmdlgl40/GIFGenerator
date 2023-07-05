import imageio
from PIL import Image
import pillow

image_list = list()
frames = list()

while True:
    images = input("Resim lokasyonlarını giriniz(hepsini hirdikten sonra 'q' ya basın):")
    if images == "q":
        break
    else:
        image_list.append(images)

for image_path in image_list:
    img = Image.open(image_path)
    resized_img = img.resize((400, 400))
    frames.append(resized_img)

imageio.mimsave("animasyon.gif", frames, format="GIF", duration=1.5)