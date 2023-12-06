from PIL import Image
import os
import json
# Counters
convertCounter = 0
fileCounter = 0


def convert():
  for file in os.listdir("data"):
    global i
    i += 1
    image = Image.open(f"data/{file}")
    new = image.resize((10, 10))
    new.save(f"data/framesNEWERRRR{i}.png")
    print(f"Succeessfully resized image{i}")

framesDict = {}
for file in os.listdir("data"):
  fileCounter += 1
  print(fileCounter)
  currentFrameArray = []
  image = Image.open(f"data/{file}")
  width, height = image.size
  pixels = image.load()
  for x in range(width):
    for y in range(height):  
      r, g, b = pixels[x, y]
      if (r,g,b) >= (255/2,255/2,255/2): 
        currentFrameArray.append(0) 
      else: 
        currentFrameArray.append(1)
    framesDict[fileCounter] = currentFrameArray
  # If the pixel is black, add the pixel to the array
with open("frameArray.json", "w") as f:
  dump = json.dump(framesDict, f)
  
  


  
