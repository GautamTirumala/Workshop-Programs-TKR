import urllib.request
import cv2 as cv
import numpy as np

url="htpp://100.69.40.16.8080"
while True:
    imgResp= urllib.request.urlopen(url)

    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    print(imgNp)

    img = cv.imdecode(imgNp,-1)

    img=cv.resize(img,(1200,800))

    cv.imshow("ipwebCam",img)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break
