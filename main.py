# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

white = (255, 255, 255)
black = (0, 0, 0)
font = cv2.FONT_HERSHEY_SIMPLEX
textThickness = 2
fontScale = 1
pillowFont = ImageFont.truetype("C:\\Users\\Aitor\\Desktop\\Programme.ttf", 50)
def createImage(pathToFile, songText, songAutor, songName):
    print("Iniciando creacion imagen")
    img = cv2.imread(pathToFile)

    #conversion to pillow(needed to write with custom font)
    cv2ImgArray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    width, height, channels = img.shape
    print("Image data: ", height, width, channels)

    lyricPosX = 50
    lyricPosY = (height-200)
    lyricPos = (lyricPosX, lyricPosY)

    cv2ImgArray = writeTextWithBackgroundPillow(cv2ImgArray, songText, white, white, lyricPosX, lyricPosY)
    cv2ImgArray = writeTextWithoutBackground(cv2ImgArray,  songAutor + " \"" + songName + "\"", lyricPosX, lyricPosY+75)

    cv2.imwrite("C:\\Users\\Aitor\\Desktop\\final.jpg", cv2ImgArray)
    cv2.waitKey(0)


def writeTextWithBackgroundPillow(cv2ImageArray,text, textColor, bgColor, posX, posY):
    textUbication, textHeight = cv2.getTextSize(text, font, fontScale, textThickness)
    pillowImage = Image.fromarray(cv2ImageArray)
    pillowDrawType = ImageDraw.Draw(pillowImage)
    pillowDrawType.rectangle([(posX, posY),(posX+925, posY+50)], fill="#FFF")
    pillowDrawType.text((posX, posY), text, font=pillowFont, fill="#000")
    cv2ImageArray = cv2.cvtColor(np.array(pillowImage), cv2.COLOR_RGB2BGR)
    return cv2ImageArray

def writeTextWithoutBackground(cv2ImageArray, text, posX, posY):
    pillowImage = Image.fromarray(cv2ImageArray)
    pillowDrawType = ImageDraw.Draw(pillowImage)
    pillowDrawType.text((posX, posY), text, font=pillowFont, fill="#FFF")
    cv2ImageArray = cv2.cvtColor(np.array(pillowImage), cv2.COLOR_RGB2BGR)
    return cv2ImageArray



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    createImage("C:\\Users\\Aitor\\Desktop\\surimi.jpg","yo te cojo y te mato y te mando al carajo", "Space Surimi", "Romantic Bogavantic")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
