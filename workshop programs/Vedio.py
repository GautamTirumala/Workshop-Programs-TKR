import cv2 as cv
video=cv.VideoCapture(0)


while(1):
    ret , frame = video.read()
    frame = cv.resize(frame,(500,300))
    cv.imshow('input video', frame)
    canny = cv.Canny(frame, 10, 175)
    cv.imshow('Canny Edges', canny)

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray', gray)

    blur = cv.GaussianBlur(gray, (15,15), cv.BORDER_DEFAULT)
    cv.imshow('Blur', blur)

    canny = cv.Canny(gray, 10, 175)
    cv.imshow('Canny Gray Edges', canny)

    if cv.waitKey(1) & 0xFF ==ord('s'):
     break

print('cancelled')
video.release()
cv.destroyAllWindows()