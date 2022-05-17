import pytesseract as py
import cv2 as cv
import os
from PIL import Image
from gtts import gTTS

py.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv.imread('image.jpg',cv.IMREAD_COLOR)
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
gray = cv.bilateralFilter(gray, 11, 17, 17)

original = py.image_to_string(gray , config= '-l eng --oem 3 --psm 12')
print(original)
file=open('abc.text','w')
myString=original
file.write(myString)

file.close()
print('text saved')
language='en'
speech=gTTS(text=myString,lang=language,slow=False)
speech.save('text.mp3')
os.system('start text.mp3')
