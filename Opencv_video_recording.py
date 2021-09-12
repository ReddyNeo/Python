import cv2

video = cv2.VideoCapture(0)
a = 1
while True:
    a = a + 1
    check, frame = video.read()  # capturing video in array formate
    print(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('capt', frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
print(a)
video.release()
cv2.destroyAllWindows()
