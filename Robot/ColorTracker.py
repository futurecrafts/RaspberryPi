import cv2
import numpy as np
import os
import sys    
import termios
import fcntl
import RPi.GPIO as gpio
import time

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

def getch():
    import sys, tty
    init()
    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of yellow color in HSV for tennis ball
    lower_yellow = np.array([30, 60, 165], dtype=np.uint8)
    upper_yellow = np.array([40, 120, 255], dtype=np.uint8)


    # Threshold the HSV image to get only yellow colors
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    moments = cv2.moments(mask)
    area = moments['m00']

    if(area > 100000): 
        #determine the x and y coordinates of the center of the object 
        #we are tracking by dividing the 1, 0 and 0, 1 moments by the area 
        x = moments['m10'] / area
        y = moments['m01'] / area

        print 'x: ' + str(int(x)) + ' y: ' + str(int(y)) + ' area: ' + str(area)
        frame = cv2.circle(frame,(int(x), int(y)), 2, (255, 255, 255), 20)
        move_pet(round(x, -1),y,round(area, -5))
        time.sleep(0.15)
    
    #cv2.imshow('mask',mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        clean_up()
        sys.exit()




def move_pet(x,y,area):
    if x > 330:
       pivot_right((x-320)/(320*12))
    elif x < 310:
       pivot_left((320-x)/(320*12))
    elif ((310 <= x <= 330) and area<1500000):
       forward(0.05)
    elif ((310 <= x <= 330) and area>4000000):
       reverse(0.05)

def init():
    gpio.setmode(gpio.BCM)
	gpio.setwarnings(False)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)

def forward(tf):
    gpio.output(17, gpio.HIGH)
    gpio.output(22, gpio.LOW)
    gpio.output(23, gpio.HIGH)
    gpio.output(24, gpio.LOW)
    time.sleep(tf)
    clean_up()
    

def reverse(tf):
    gpio.output(17, gpio.LOW)
    gpio.output(22, gpio.HIGH)
    gpio.output(23, gpio.LOW)
    gpio.output(24, gpio.HIGH)
    time.sleep(tf)
    clean_up()

def turn_left(tf):
    gpio.output(17, gpio.LOW)
    gpio.output(22, gpio.LOW)
    gpio.output(23, gpio.HIGH)
    gpio.output(24, gpio.LOW)
    time.sleep(tf)
    clean_up()

def turn_right(tf):
    gpio.output(17, gpio.HIGH)
    gpio.output(22, gpio.LOW)
    gpio.output(23, gpio.LOW)
    gpio.output(24, gpio.LOW)
    time.sleep(tf)
    clean_up()

def pivot_left(tf):
    gpio.output(17, gpio.LOW)
    gpio.output(22, gpio.LOW)
    gpio.output(23, gpio.HIGH)
    gpio.output(24, gpio.LOW)
    time.sleep(tf)
    clean_up()

def pivot_right(tf):
    gpio.output(17, gpio.HIGH)
    gpio.output(22, gpio.LOW)
    gpio.output(23, gpio.LOW)
    gpio.output(24, gpio.LOW)
    time.sleep(tf)
    clean_up()

def clean_up():
    gpio.output(17, gpio.LOW)
    gpio.output(22, gpio.LOW)
    gpio.output(23, gpio.LOW)
    gpio.output(24, gpio.LOW)
    #gpio.cleanup()   

def main():
    while True:
        getch()
    cv2.destroyAllWindows()
	gpio.cleanup()



if __name__ == "__main__":
    main()