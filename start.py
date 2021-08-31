from PIL import Image

i = Image.open('pup1.png')
i.convert(mode='L').save('pup1_bw.webp')
