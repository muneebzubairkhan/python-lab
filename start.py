from PIL import Image
import os

size_300 = (300, 300)
size_700 = (700, 700)

for f in os.listdir('.'):
    if f.endswith('.png'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)

        i.thumbnail(size_300)
        i.save('webp_size_300/' + fn + '.webp')

        i.thumbnail(size_700)
        i.save('webp_size_700/' + fn + '.webp')
