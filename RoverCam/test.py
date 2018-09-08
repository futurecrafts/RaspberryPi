import RPi.GPIO as GPIO
from time import sleep

pin1 = 17
pin2 = 22
pin3 = 23
pin4 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)

#Forward
GPIO.output(pin1, GPIO.HIGH)
GPIO.output(pin2, GPIO.LOW)
GPIO.output(pin3, GPIO.HIGH)
GPIO.output(pin4, GPIO.LOW)

sleep(2)
#Backward
GPIO.output(pin1, GPIO.LOW)
GPIO.output(pin2, GPIO.HIGH)
GPIO.output(pin3, GPIO.LOW)
GPIO.output(pin4, GPIO.HIGH)

sleep(2)
#Left
GPIO.output(pin1, GPIO.LOW)
GPIO.output(pin2, GPIO.LOW)
GPIO.output(pin3, GPIO.HIGH)
GPIO.output(pin4, GPIO.LOW)

sleep(2)
#Right
GPIO.output(pin1, GPIO.HIGH)
GPIO.output(pin2, GPIO.LOW)
GPIO.output(pin3, GPIO.LOW)
GPIO.output(pin4, GPIO.LOW)

sleep(2)

GPIO.cleanup()
