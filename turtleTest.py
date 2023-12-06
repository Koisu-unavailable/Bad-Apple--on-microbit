from PIL import Image
import json
class imageTester():
    def __init__(self) -> None:
        test = Image.new(mode="RGB", size=(10,10))
        test.show()
        pixels = test.load()
        for x in range(test.width):
            for y in range(test.height):
                pixels[x,y] = (255,255,255)
                test.show()
test = imageTester()
    