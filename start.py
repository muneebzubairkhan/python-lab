from PIL import Image

i = Image.open('pup1.png')
i.rotate(45).save('pup1_rotate1.webp')
