"""playsound_with_pir.py: Trigger script for playing sound with PIR sensor."""
# To increase volume=>  amixer  sset PCM,0 90%

__author__ = "FutureCrafts"
__email__ = "futurecrafts.yb@gmail.com"

import pyttsx

import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
PIR = 20

print "Starting PIR Sensor..."
 
#set GPIO direction (IN / OUT)
GPIO.setup(PIR, GPIO.IN)

engine = pyttsx.init()

try:
    time.sleep(2)
    while True:
        if GPIO.input(PIR):
            print "Motion Detected..."
            engine.say('Good morning.')
            engine.runAndWait()
            time.sleep(2)
        time.sleep(0.1)
        
except:
    GPIO.cleanup()
