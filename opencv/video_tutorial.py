import numpy as np
import cv2

# load video or open webcam
# argument can file video
# 0 for default webcam
# 1 for usb webcam
cap = cv2.VideoCapture(0)

while True:
    # capture frame-by-frame
    _, frame = cap.read()    

    # convert frame color to GRAY
    # few options for arg 2:
    #     - cv2.COLOR_BGR2GRAY
    #     - cv2.COLOR_BGR2HSV
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # flips the frame
    # 0 - vertically
    # 1 - horizontally
    gray = cv2.flip(gray, 1)

    # display the resulting frame
    cv2.imshow('Video', frame)
    cv2.imshow('Gray', gray)


    
    # keyboard binding
    # within 1 millisecond, user must press 'k'
    # to break out of loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture

# release capture
cap.release()

# destroy windows
cv2.destroyAllWindows()

