import cv2 , time

video = cv2.VideoCapture(0)
check, frame = video.read() # capturing video in array formate
print(check)
print(frame)
cv2.imshow('capt', frame)
cv2.waitKey(600000)

video.release()
time.sleep(3)  # video will be passed 3 sec
cv2.destroyAllWindows()
