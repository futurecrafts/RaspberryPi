import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIR = 20

print "Start PIR Sensor"

GPIO.setup(PIR, GPIO.IN)

try:
    time.sleep(2)
    while True:
        if GPIO.input(PIR):
            print "Motion Detected..."
            time.sleep(5)
        time.sleep(0.1)
        
except:
    GPIO.cleanup()
