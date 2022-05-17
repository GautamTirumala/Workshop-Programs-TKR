import pytesseract
import cv2 as cv
import os
from PIL import Image
from gtts import gTTS

pytesseract.pytesseract.trsseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'

img = cv.imread('image.jpg',cv.IMREAD_COLOR)
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
gray = cv.bilateralFilter(gray, 11, 17, 17)

original = pytesseract.image_to_string(gray ,lang='eng', config='-l eng --oem 3 --psm 12')

#image_to_string(gray , config='-1 eng --oem 3 --psm 12')

#pytesseract.image_to_string(export_image ,lang='eng', config='--psm 13 --oem 1 -c tessedit_char_whitelist=ABCDEFG0123456789')
print(original)
file=open('abc.text','w')
myString=original
file.write(myString)

file.close()
print('text saved')
language='eng'
speech=gTTS(text=myString,lang=language,slow=False)
speech.save('text.mp3')
os.system('start text.mp3')