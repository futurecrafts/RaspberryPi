import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
from time import sleep

def init():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)

def clean():
        GPIO.output(17, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)

def on_connect(self, client, userdata, rc):
        print("Connected with result code " + str(rc))
        self.subscribe("home/esp/node03/servo")

def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))
        if msg.payload == "0":
                GPIO.output(17, GPIO.HIGH)
                GPIO.output(22, GPIO.LOW)
                GPIO.output(23, GPIO.HIGH)
                GPIO.output(24, GPIO.LOW)
                sleep(2)
                clean()
		if msg.payload == "1":
                GPIO.output(17, GPIO.LOW)
                GPIO.output(22, GPIO.HIGH)
                GPIO.output(23, GPIO.LOW)
                GPIO.output(24, GPIO.HIGH)
                sleep(2)
                clean()
        if msg.payload == "2":
                GPIO.output(17, GPIO.LOW)
                GPIO.output(22, GPIO.LOW)
                GPIO.output(23, GPIO.HIGH)
                GPIO.output(24, GPIO.LOW)
                sleep(2)
                clean()
        if msg.payload == "3":
                GPIO.output(17, GPIO.HIGH)
                GPIO.output(22, GPIO.LOW)
                GPIO.output(23, GPIO.LOW)
                GPIO.output(24, GPIO.LOW)
                sleep(2)
                clean()

init()
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("10.1.1.8", 1883, 60)

client.loop_forever()
GPIO.cleanup()
