from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def clean():
  GPIO.output(17, GPIO.LOW)
  GPIO.output(22, GPIO.LOW)
  GPIO.output(23, GPIO.LOW)
  GPIO.output(24, GPIO.LOW)
        
def valmap(x, in_min, in_max, out_min, out_max):
  return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)
    
def forward():
  GPIO.output(17, GPIO.HIGH)
  GPIO.output(22, GPIO.LOW)
  GPIO.output(23, GPIO.HIGH)
  GPIO.output(24, GPIO.LOW)
  
def backward():
  GPIO.output(17, GPIO.LOW)
  GPIO.output(22, GPIO.HIGH)
  GPIO.output(23, GPIO.LOW)
  GPIO.output(24, GPIO.HIGH)

def carmove(x, y):
  m1 = GPIO.PWM(25, 100)
  m2 = GPIO.PWM(26, 100)
  motorSpeedA = 0
  motorSpeedB = 0
  m1.start(motorSpeedA)
  m2.start(motorSpeedB)
        
  if y < 90:
    forward()
    print "forward!"
    motorSpeedA = valmap(y, 90, 0, 0, 100)
    motorSpeedB = valmap(y, 90, 0, 0, 100)
  elif y > 110:
    backward()
    print "backward!"
    motorSpeedA = valmap(y, 110, 200, 0, 100)
    motorSpeedB = valmap(y, 110, 200, 0, 100)
  elif towhere == 'left':
                        GPIO.output(17, GPIO.LOW)
                        GPIO.output(22, GPIO.LOW)
                        GPIO.output(23, GPIO.HIGH)
                        GPIO.output(24, GPIO.LOW)
                        print "Rover Left"
        elif towhere == 'right':
                        GPIO.output(17, GPIO.HIGH)
                        GPIO.output(22, GPIO.LOW)
                        GPIO.output(23, GPIO.LOW)
                        GPIO.output(24, GPIO.LOW)
                        print "Rover Right"
        elif towhere == 'stop':
                        clean()
                        print "Rover Stop"
						
if __name__ == '__main__':
        import sys
        x = sys.argv[1]
        y = sys.argv[2]
        print x + " and " + y
        GPIO.setup(25, GPIO.OUT) #EN A
        GPIO.setup(26, GPIO.OUT) #EN B
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)
        carmove(x, y)
        # GPIO.cleanup()
