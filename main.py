from PIL import Image
import os
i = 0
def convert():
    for file in os.listdir("data"):
        i += 1
        image = Image.open(f"data/{file}")
        new = image.resize((10, 10))
        new.save(f"data/framesNEWERRRR{i}.png")
        print(f"Succeessfully resized image{i}")
   
for file in os.listdir("data"):
    arr = []
    image = Image.open(f"data/{file}")
    pixels = image.load()
    for pixel, pixely, in pixels:
        if 
    