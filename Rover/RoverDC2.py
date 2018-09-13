import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
from flask import Flask, render_template #, request, redirect, url_for, make_response
from time import sleep
import atexit

app = Flask(__name__) # set up flask server

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

# when the root IP is selected, return rover.html page
@app.route('/')
def index():
        init()
        try:
          return render_template('rover2.html')
        except Exception as e:
          print e
          pass

#@app.route("/<reset>")
def reset():
        GPIO.cleanup()

# receive direction from the button press on rover.html
@app.route("/<direction>") # , method=['POST']
def move(direction):
                # Choose the direction of the request
                if direction == 'go':
                        GPIO.output(17, GPIO.HIGH)
                        GPIO.output(22, GPIO.LOW)
                        GPIO.output(23, GPIO.HIGH)
                        GPIO.output(24, GPIO.LOW)
                        #sleep(2)
                        #clean()
                        print "Rover Go"
                elif direction == 'back':
                        GPIO.output(17, GPIO.LOW)
                        GPIO.output(22, GPIO.HIGH)
                        GPIO.output(23, GPIO.LOW)
                        GPIO.output(24, GPIO.HIGH)
                        #sleep(2)
                        #clean()
                        print "Rover Back"
                elif direction == 'left':
                        GPIO.output(17, GPIO.LOW)
                        GPIO.output(22, GPIO.LOW)
                        GPIO.output(23, GPIO.HIGH)
                        GPIO.output(24, GPIO.LOW)
                        #sleep(2)
                        #clean()
                        print "Rover Left"
                elif direction == 'right':
                        GPIO.output(17, GPIO.HIGH)
                        GPIO.output(22, GPIO.LOW)
                        GPIO.output(23, GPIO.LOW)
                        GPIO.output(24, GPIO.LOW)
                        #sleep(2)
                        #clean()
                        print "Rover Right"
                elif direction == 'stop':
                        clean()
                        print "Rover Stop"

                return direction

                # or
                #  response = make_response(redirect(url_for('index')))
                # return(response)

# Clean everything up when the app exits
atexit.register(reset)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=9000, debug=True)

