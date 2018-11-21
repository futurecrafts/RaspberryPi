import os
import RPi.GPIO as GPIO
#import paho.mqtt.client as mqtt
from flask import Flask, render_template, request # , redirect, url_for, make_response
from time import sleep
import atexit

app = Flask(__name__) # set up flask server

def init():
        print "init started"

# when the root IP is selected, return RoverControlWithBox.html page
@app.route('/')
def index():
        init()
        try:
          return render_template('RoverControlWithBox.html')
        except Exception as e:
          print e
          pass

#@app.route("/<reset>")
def reset():
        GPIO.cleanup()
        print "reset"

# receive servo value
@app.route("/servopos")
def servopos():
        horValue = request.args.get('servolr', None)
        verValue = request.args.get('servodu', None)
        print "servopos received"
        print horValue + " and " + verValue
	    os.system("python servocontrol.py 4 " + horValue + " 2 " + verValue)
        return "OK"

# receive car value
@app.route("/carpos")
def carpos():
        horValue = request.args.get('carlr', None)
        verValue = request.args.get('cardu', None)
        print "carpos received"
        print horValue + " and " + verValue
	    os.system("python motorcontrol.py " + horValue + " " + verValue)
        return "OK"


# Clean everything up when the app exits
atexit.register(reset)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=9000, debug=True)