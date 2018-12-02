from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def clean():
        GPIO.output(12, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(19, GPIO.LOW)
        GPIO.output(26, GPIO.LOW)

def carmove(towhere):
        if towhere == 'go':
                        GPIO.output(12, GPIO.HIGH)
                        GPIO.output(13, GPIO.LOW)
                        GPIO.output(19, GPIO.HIGH)
                        GPIO.output(26, GPIO.LOW)
                        print "Rover Go"
        elif towhere == 'back':
                        GPIO.output(12, GPIO.LOW)
                        GPIO.output(13, GPIO.HIGH)
                        GPIO.output(19, GPIO.LOW)
                        GPIO.output(26, GPIO.HIGH)
                        print "Rover Back"
        elif towhere == 'left':
                        GPIO.output(12, GPIO.LOW)
                        GPIO.output(13, GPIO.LOW)
                        GPIO.output(19, GPIO.HIGH)
                        GPIO.output(26, GPIO.LOW)
                        print "Rover Left"
        elif towhere == 'right':
                        GPIO.output(12, GPIO.HIGH)
                        GPIO.output(13, GPIO.LOW)
                        GPIO.output(19, GPIO.LOW)
                        GPIO.output(26, GPIO.LOW)
                        print "Rover Right"
        elif towhere == 'stop':
                        clean()
                        print "Rover Stop"
						
if __name__ == '__main__':
        import sys
        towhere = sys.argv[1]
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(19, GPIO.OUT)
        GPIO.setup(26, GPIO.OUT)
        carmove(towhere)
        #GPIO.cleanup()
