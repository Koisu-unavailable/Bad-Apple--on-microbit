from PIL import Image
import os
i = 0
for file in os.listdir("data"):
    i += 1
    image = Image.open(f"data/{file}")
    new = image.resize((10, 10))
    new.show()
    new.save(f"data/framesNEWERRRR{i}.png")
    print(f"Succeessfully resized image{i}")
    
    