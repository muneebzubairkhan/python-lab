from PIL import Image
import os

for f in os.listdir('.'):
    if f.endswith('.png'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.save('webp_folder/' + fn + '.webp')
