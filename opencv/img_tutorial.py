# import numerical python library
import numpy as np
# import opencv
import cv2


# load an image
# argument 2 options:
#  1 cv2.IMREAD_COLOR
#  0 cv2.IMREAD_GRAYSCALE
# -1 cv2.IMREAD_UNCHANGED
img = cv2.imread('wsu_tank.jpg', 0)

# (optional) change size of the image
height, width = img.shape[:2]
print img.shape

# interpolation -> is a method of constructing new data points
#                  within the range of a discrete set of known data points
# INTER_NEAREST, INTER_LINEAR, INTER_AREA, INTER_CUBIC, etc
# INTER_CUBIC a bicubic interpolation over 4x4 pixel neighborhood
img = cv2.resize(img, (width/4, height/4), interpolation=cv2.INTER_CUBIC)

# show that img is just an array or matrix
print img
print type(img) # prints data type of img


# display image in a window
cv2.imshow('The Picture', img)

# keyboard binding
# argument is time in milliseconds for any keyboard event
# any key in that time, program continues
# 0 waits indefinitely
k = cv2.waitKey(0) # & 0xFF

# wait for ESC key to exit
if k == 27: 
    # destroy all windows
    # provide an alternative
    cv2.destroyAllWindows()

# wait for 's' key to save and exit
elif k == ord('s'): 
    cv2.imwrite('wsu_tank_gray.jpg', img)
    cv2.destroyWindow('The Picture')
