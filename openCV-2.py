import cv2

cam = cv2.VideoCapture(0)
while True:
    _,frame = cam.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("my WEBCAM",frame)
    cv2.moveWindow("my WEBCAM",0,0)
    cv2.imshow("my grayFrame",gray)
    cv2.moveWindow("my grayFrame",640,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break