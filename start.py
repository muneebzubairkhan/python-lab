from PIL import Image, ImageFilter

i = Image.open('pup1.png')
i.filter(ImageFilter.GaussianBlur(radius=15)).save('pup1_blur.webp')
