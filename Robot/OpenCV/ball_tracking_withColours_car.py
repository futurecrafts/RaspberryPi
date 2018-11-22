from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time
import os
import RPi.GPIO as GPIO

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
        help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
        help="max buffer size")
args = vars(ap.parse_args())

greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
yellowLower = np.array([30, 60, 165], dtype=np.uint8)
yellowUpper = np.array([40, 120, 255], dtype=np.uint8)
redLower = (0, 50, 50)
redUpper = (10, 255, 255)
pts = deque(maxlen=args["buffer"])

if not args.get("video", False):
        vs = VideoStream(src=0).start()
else:
        vs = cv2.VideoCapture(args["video"])
        vs.set(3, 600)
        vs.set(4, 600)
time.sleep(2.0)

def move_car(x, y, radius):
  if x > 400:
    period = float((x-300)/(300*5))
    os.system("python motorcontrol2.py pright " + str(period))
    print period
  elif x < 200:
    period = float((300-x)/(300*5))
    os.system("python motorcontrol2.py pleft " + str(period))
    print period
  elif ((200 <= x <= 400) and radius<80):
    os.system("python motorcontrol2.py go " + str(0.3))
    print "car go"
  elif ((200 <= x <= 400) and radius>100):
    os.system("python motorcontrol2.py back " + str(0.3))
    print "car back"

while True:
  frame = vs.read()
  frame = frame[1] if args.get("video", False) else frame
  if frame is None:
    break
  #frame = imutils.resize(frame, width=600)
  blurred = cv2.GaussianBlur(frame, (11, 11), 0)
  hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
  
  mask = cv2.inRange(hsv, redLower, redUpper)
  mask = cv2.erode(mask, None, iterations=2)
  mask = cv2.dilate(mask, None, iterations=2)

  cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  cnts = cnts[0] if imutils.is_cv2() else cnts[1]
  center = None
  #print 'cnts got: '
  #print len(cnts)
  if len(cnts) > 0:
  # find the largest contour in the mask, then use it to compute the minimum encl$
    c = max(cnts, key=cv2.contourArea)
    ((x, y), radius) = cv2.minEnclosingCircle(c)
    M = cv2.moments(c)
    print 'distance: '
    print M["m00"]
    Dist = M["m00"]
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    center = (cX, cY)
    print 'center: '
    print center
        # only proceed if the radius meets a minimum size
    print 'radius: '
    print radius
    if radius > 10:
    # draw the circle and centroid on the frame, then update the list of tracked $
      cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
      cv2.circle(frame, center, 5, (0, 0, 255), -1)
      move_car(round(cX), round(cY), round(radius))
      #time.sleep(0.3)
      #print 'circle drawing and passing to car now'

  time.sleep(1)
  # update the points queue
  #pts.appendleft(center)

  # loop over the set of tracked points
  #for i in range(1, len(pts)):
  # if either of the tracked points are None, ignore them
  #  if pts[i - 1] is None or pts[i] is None:
   #   continue

    # otherwise, compute the thickness of the line and draw the connecting lines
    #thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
	#cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)

  # show the frame to our screen
  #cv2.imshow("Frame", frame)
  #key = cv2.waitKey(1) & 0xFF

  # if the 'q' key is pressed, stop the loop
  #if key == ord("q"):
  #       break


if not args.get("video", False):
  vs.stop()
else:
  vs.release()

GPIO.cleanup()
cv2.destroyAllWindows()
