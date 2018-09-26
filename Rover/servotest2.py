import RPi.GPIO as GPIO
from time import sleep

servo = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)

pwm=GPIO.PWM(servo,50)
pwm.start(0)

pwm.ChangeDutyCycle(2)
sleep(2);
pwm.ChangeDutyCycle(5)
sleep(2);
pwm.ChangeDutyCycle(8)
sleep(2);
pwm.ChangeDutyCycle(11)
sleep(2);
pwm.ChangeDutyCycle(8)
sleep(2);
pwm.ChangeDutyCycle(5)
sleep(2);
pwm.ChangeDutyCycle(2)
sleep(2)
pwm.ChangeDutyCycle(0)

pwm.stop()
GPIO.cleanup()
