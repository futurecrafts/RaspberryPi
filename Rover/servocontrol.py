from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def setServoAngle(servo1, angle1, servo2, angle2):
        assert angle >=0 and angle <= 180
        pwm1 = GPIO.PWM(servo1, 50)
        pwm2 = GPIO.PWM(servo2, 50)
        pwm1.start(0)
        pwm2.start(0)
        dutyCycle1 = angle1 / 18. + 2.
        dutyCycle2 = angle2 / 18. + 2.
        pwm1.ChangeDutyCycle(dutyCycle1)
        pwm2.ChangeDutyCycle(dutyCycle2)
        sleep(0.5)
        pwm1.ChangeDutyCycle(0)
        pwm2.ChangeDutyCycle(0)
        pwm1.stop()
        pwm2.stop()

if __name__ == '__main__':
        import sys
        servo1 = int(sys.argv[1])
        servo2 = int(sys.argv[3])
        GPIO.setup(servo1, GPIO.OUT)
        GPIO.setup(servo2, GPIO.OUT)
        setServoAngle(servo1, int(sys.argv[2]), servo2, int(sys.argv[4]))
        # GPIO.cleanup()
