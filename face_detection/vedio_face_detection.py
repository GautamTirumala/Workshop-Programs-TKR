import cv2 as cv
import mouse
video=cv.VideoCapture(0)





while(1):
    ret , frame = video.read()
    frame = cv.resize(frame,(600,400))
    cv.imshow('input video', frame)

    haar_cascade = cv.CascadeClassifier('haarEye.xml')
    faces_rect = haar_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)
    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w,y+h), (150,25,255), thickness=2)

    cv.imshow('Detected Faces', frame)

    print(f'Number of eyes found = {len(faces_rect)}')

    if cv.waitKey(1) & 0xFF ==ord('s'):
     break
    mouse.click('right')



print('cancelled')
video.release()
cv.destroyAllWindows()