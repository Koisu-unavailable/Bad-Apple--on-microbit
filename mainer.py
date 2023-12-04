from PIL import Image
import os

i = 0


def convert():
  for file in os.listdir("data"):
    global i
    i += 1
    image = Image.open(f"data/{file}")
    new = image.resize((10, 10))
    new.save(f"data/framesNEWERRRR{i}.png")
    print(f"Succeessfully resized image{i}")


for file in os.listdir("data"):
  arr = []
  image = Image.open(f"data/{file}")
  pixels = image.load()
  # If the pixel is black, add the pixel to the array
  for i, j, in pixels:
    if pixels[i, j] == (0, 0, 0) or pixels[i, j] == (225, 255, 255):
      arr.append((i, j))
  print(arr)
  with open("vectors.txt", "a") as f:
    f.write(f"{arr}\n")
  
