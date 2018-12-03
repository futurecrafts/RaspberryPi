from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def clean():
  GPIO.output(12, GPIO.LOW)
  GPIO.output(13, GPIO.LOW)
  GPIO.output(19, GPIO.LOW)
  GPIO.output(26, GPIO.LOW)
        
def valmap(x, in_min, in_max, out_min, out_max):
  return int((int(x)-int(in_min)) * (int(out_max)-int(out_min)) / (int(in_max)-int(in_min)) + int(out_min))
    
def forward():
  GPIO.output(12, GPIO.HIGH)
  GPIO.output(13, GPIO.LOW)
  GPIO.output(19, GPIO.HIGH)
  GPIO.output(26, GPIO.LOW)
  
def backward():
  GPIO.output(12, GPIO.LOW)
  GPIO.output(13, GPIO.HIGH)
  GPIO.output(19, GPIO.LOW)
  GPIO.output(26, GPIO.HIGH)

def carmove(x_str, y_str):
  x = int(x_str)
  y = int(y_str)
  m1 = GPIO.PWM(16, 100)
  m2 = GPIO.PWM(20, 100)
  motorSpeedA = 0
  motorSpeedB = 0
  m1.start(motorSpeedA)
  m2.start(motorSpeedB)
  print x
  print y
  # Y-axis used for forward and backward control      
  if y < 90:
        forward()
        print "Forward!"
        motorSpeedA = valmap(y, 90, 0, 0, 100)
        motorSpeedB = valmap(y, 90, 0, 0, 100)
  elif y > 110:
        backward()
        print "Backward!"
        motorSpeedA = valmap(y, 110, 200, 0, 100)
        motorSpeedB = valmap(y, 110, 200, 0, 100)
  else:
	print "Stay!"
	motorSpeedA = 0
	motorSpeedB = 0
  
  # X-axis used for left and right control
  if x < 90:
	print "Left!"
	mapped = valmap(x, 90, 0, 0, 100)
	# Move to left - decrease left motor speed, increase right motor speed
	motorSpeedA = motorSpeedA - mapped
	motorSpeedB = motorSpeedB + mapped
	if motorSpeedA < 0:
		motorSpeedA = 0
	if motorSpeedB > 100:
		motorSpeedB = 100
  elif x > 110:
	print "Right!"
	mapped = valmap(x, 110, 200, 0, 100)
	# Move right - decrease right motor speed, increase left motor speed
	motorSpeedA = motorSpeedA + mapped
	motorSpeedB = motorSpeedB - mapped
	if motorSpeedA > 100:
		motorSpeedA = 100
	if motorSpeedB < 0:
		motorSpeedB = 0
		
  # Prevent buzzing at low speeds (Adjust according to your motors. My motors couldn't start moving if PWM value was below value of 70)
  #if motorSpeedA < 10:
	#motorSpeedA = 0
  #if motorSpeedB < 10:
        #motorSpeedB = 0;
	
  m1.ChangeDutyCycle(motorSpeedA)
  m2.ChangeDutyCycle(motorSpeedB)
  print str(motorSpeedA) + " and " + str(motorSpeedB)
  sleep(0.5)
  m1.stop()
  m2.stop()
	
	
if __name__ == '__main__':
        import sys
        x = sys.argv[1]
        y = sys.argv[2]
        print x + " and " + y
        GPIO.setup(16, GPIO.OUT) #EN A
        GPIO.setup(20, GPIO.OUT) #EN B
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(19, GPIO.OUT)
        GPIO.setup(26, GPIO.OUT)
        carmove(x, y)
        # GPIO.cleanup()
