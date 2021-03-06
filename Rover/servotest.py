import RPi.GPIO as GPIO
from time import sleep

servo = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)

pwm=GPIO.PWM(servo,50)
pwm.start(0)

def SetAngle(angle):
        duty = angle / 18 + 2
        GPIO.output(servo, True)
        pwm.ChangeDutyCycle(duty)
        sleep(1)
        GPIO.output(servo, False)
        pwm.ChangeDutyCycle(0)

SetAngle(45)
sleep(2)
SetAngle(90)
sleep(2)
SetAngle(45)
sleep(2)
pwm.stop()
GPIO.cleanup()
