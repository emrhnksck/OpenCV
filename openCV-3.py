import cv2

cam = cv2.VideoCapture(0)
width = 1280
height = 720
while True:
    _,frame = cam.read()
    cv2.imshow('my cam',frame)
    cv2.moveWindow('my cam',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()