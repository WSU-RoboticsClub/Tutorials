import cv2
import numpy as np


def searchForMovement(filteredImage, cameraFeed):
    global xpos, ypos
    # Retrieves all contours
    #contours, hierarchy = cv2.findContours(filteredImage, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    # Retrieves external contours
    contours, hierarchy = cv2.findContours(filteredImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    objectDetected = False

    if len(contours) > 0:
        objectDetected = True
    else:
        objectDetected = False

    
    if objectDetected:
        # largest contour is found at the end of the contours vector
        # assume that the biggest contour is the object we are looking for
        largest = contours[len(contours)-1]
        # make bounding rectangle around the largest contour then find its centroid
        x,y,w,h = cv2.boundingRect(largest)
        xpos = x + w/2
        ypos = y + h/2
        
    x = xpos
    y = ypos

    #draw some crosshairs around the object
    cv2.circle(cameraFeed,(x,y),20,(0,255,0),2)
    cv2.line(cameraFeed,(x,y),(x,y-25),(0,255,0),2)
    cv2.line(cameraFeed,(x,y),(x,y+25),(0,255,0),2)
    cv2.line(cameraFeed,(x,y),(x-25,y),(0,255,0),2)
    cv2.line(cameraFeed,(x,y),(x+25,y),(0,255,0),2)

    #write the position of the object to the screen
    cv2.putText(cameraFeed,"Tracking object at (" + str(x)+","+str(y)+")",(x,y),1,1,(255,0,0),2)



SENSITIVITY_VAL = 30
BLURSIZE = 10
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
debugMode = True
xpos = 0
ypos = 0

cap = cv2.VideoCapture(0)
# 3 horizontal pixels, 4 vertical pixels, 5 frame rate
cap.set(3, FRAME_WIDTH)
cap.set(4, FRAME_HEIGHT)

while(1):

    # Get 1st frame
    _, frame1 = cap.read()
    # (optional) flip
    frame1 = cv2.flip(frame1, 1)
    # Convert 1st frame to gray
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    # Get 2nd frame
    _, frame2 = cap.read()
    # (optional) flip
    frame2 = cv2.flip(frame2, 1)
    # Convert 2nd frame to gray
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # get difference between two frames
    diffImage = cv2.absdiff(gray1, gray2)


    if debugMode:
        # show difference image
        cv2.imshow('Difference Image', diffImage)

    # get threshold of image, to convert to 1's and 0's
    _, thresImage = cv2.threshold(diffImage, SENSITIVITY_VAL, 255, cv2.THRESH_BINARY)

    if debugMode:
        # show threshold image
        cv2.imshow('Threshold Image', thresImage)

    # blur image to get rid of white specs and make object bolder
    blurImage = cv2.blur(thresImage, (BLURSIZE,BLURSIZE))
    # threshold blur image to convert to 1's and 0's
    _, blurImage = cv2.threshold(blurImage, SENSITIVITY_VAL, 255, cv2.THRESH_BINARY)

    if debugMode:
        # show blur image
        cv2.namedWindow('Blur Image', cv2.WINDOW_NORMAL)
        #cv2.resizeWindow('Blur Image', 640, 480)
        cv2.imshow('Blur Image', blurImage)

    # target movement
    searchForMovement(blurImage, frame1)


    cv2.imshow('frame1',frame1)

    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
