from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
        help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
        help="max buffer size")
args = vars(ap.parse_args())

greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
yellowLower = (30, 60, 165)
yellowUpper = (40, 120, 255)
redLower = (0, 50, 50)
redUpper = (10, 255, 255)
pts = deque(maxlen=args["buffer"])

if not args.get("video", False):
        vs = VideoStream(src=0).start()
else:
        vs = cv2.VideoCapture(args["video"])
        vs.set(3, 600) // codes for pi zero
        vs.set(4, 600) // codes for pi zero
time.sleep(2.0)

while True:
  frame = vs.read()
  frame = frame[1] if args.get("video", False) else frame
  if frame is None:
    break
  #frame = imutils.resize(frame, width=600) ?????why => imutils cannot be install in pi zero
  blurred = cv2.GaussianBlur(frame, (11, 11), 0)
  hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
  
  mask = cv2.inRange(hsv, redLower, redUpper)
  mask = cv2.erode(mask, None, iterations=2)
  mask = cv2.dilate(mask, None, iterations=2)

  cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  cnts = cnts[0] if imutils.is_cv2() else cnts[1]
  center = None
  print 'cnts got: '
  print len(cnts)
  if len(cnts) > 0:
  # find the largest contour in the mask, then use it to compute the minimum enclosing circle and centroid
    c = max(cnts, key=cv2.contourArea)
    ((x, y), radius) = cv2.minEnclosingCircle(c)
    M = cv2.moments(c)
    print 'distance: '
    print M["m00"]
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    print 'center: '
    print center
	# only proceed if the radius meets a minimum size
    print 'radius: '
    print radius
    if radius > 10:
    # draw the circle and centroid on the frame, then update the list of tracked points
      cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
      cv2.circle(frame, center, 5, (0, 0, 255), -1)
      print 'circle drawing now'

  # update the points queue
  pts.appendleft(center)

  # loop over the set of tracked points
  for i in range(1, len(pts)):
  # if either of the tracked points are None, ignore them
    if pts[i - 1] is None or pts[i] is None:
      continue

    # otherwise, compute the thickness of the line and draw the connecting lines
    thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
	cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)

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

cv2.destroyAllWindows()
