# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import cv2

white = (255, 255, 255)
black = (0, 0, 0)
font = cv2.FONT_HERSHEY_SIMPLEX
textThickness = 2
fontScale = 1
def createImage(pathToFile, songText, songAutor, songName):
    print("Iniciando creacion imagen")
    img = cv2.imread(pathToFile)
    width, height, channels = img.shape
    print("Image data: ", height, width, channels)

    lyricPosX = 50
    lyricPosY = (height-200)
    lyricPos = (lyricPosX, lyricPosY)

    writeTextWithBackground(img, songText, black, white, lyricPosX, lyricPosY)
    cv2.putText(img, songAutor + " \"" + songName + "\"", (lyricPosX, lyricPosY+50), font, fontScale, white, textThickness, 2)

    cv2.imwrite("C:\\Users\\Aitor\\Desktop\\final.jpg", img)
    cv2.waitKey(0)

def writeTextWithBackground(img, text, textColor, bgColor, posX, posY):
    textUbication, textHeight = cv2.getTextSize(text, font, fontScale, textThickness)
    cv2.rectangle(img, (posX, posY+10), (posX+textUbication[0], posY-textUbication[1]), bgColor, -1)
    cv2.putText(img, text, (posX, posY), font, fontScale, textColor, textThickness, 2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    createImage("C:\\Users\\Aitor\\Desktop\\surimi.jpg","yo te cojo y te mato y te mando al carajo", "Space Surimi", "Romantic Bogavantic")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
