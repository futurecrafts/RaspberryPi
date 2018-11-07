from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def clean():
        GPIO.output(17, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)

def carmove(towhere):
        if towhere == 'go':
                        GPIO.output(17, GPIO.HIGH)
                        GPIO.output(22, GPIO.LOW)
                        GPIO.output(23, GPIO.HIGH)
                        GPIO.output(24, GPIO.LOW)
						time.sleep(wait)
                        print "car Go"
        elif towhere == 'back':
                        GPIO.output(17, GPIO.LOW)
                        GPIO.output(22, GPIO.HIGH)
                        GPIO.output(23, GPIO.LOW)
                        GPIO.output(24, GPIO.HIGH)
						time.sleep(wait)
                        print "car Back"
        elif towhere == 'left':
                        GPIO.output(17, GPIO.LOW)
                        GPIO.output(22, GPIO.LOW)
                        GPIO.output(23, GPIO.HIGH)
                        GPIO.output(24, GPIO.LOW)
						time.sleep(wait)
                        print "car Left"
        elif towhere == 'right':
                        GPIO.output(17, GPIO.HIGH)
                        GPIO.output(22, GPIO.LOW)
                        GPIO.output(23, GPIO.LOW)
                        GPIO.output(24, GPIO.LOW)
						time.sleep(wait)
                        print "car Right"
		elif towhere == 'pleft':
                        GPIO.output(17, GPIO.HIGH)
                        GPIO.output(22, GPIO.LOW)
                        GPIO.output(23, GPIO.LOW)
                        GPIO.output(24, GPIO.HIGH)
						time.sleep(wait)
                        print "car pivot Left"
        elif towhere == 'pright':
                        GPIO.output(17, GPIO.LOW)
                        GPIO.output(22, GPIO.HIGH)
                        GPIO.output(23, GPIO.HIGH)
                        GPIO.output(24, GPIO.LOW)
						time.sleep(wait)
                        print "car pivot Right"
        elif towhere == 'stop':
                        clean()
                        print "car Stop"
						
if __name__ == '__main__':
        import sys
        towhere = sys.argv[1]
		wait = sys.argv[2]
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)
        carmove(towhere, wait)
        #GPIO.cleanup()