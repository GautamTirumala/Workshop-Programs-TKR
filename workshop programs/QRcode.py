import pyqrCode 
import png as png
import cv2 as cv

s="www.pantechelearling.com"

url=pyqrcode.create(s)

url.svg("myqr.svg",scale=8)

url.png("myqr.png", scale=6)

out = cv.imread("myqr.png")
cv.imshow("qrcode",out)
