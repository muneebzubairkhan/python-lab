from PIL import Image
import os

for f in os.listdir('.'):
    if f.endswith('.png'):
        print(f)

