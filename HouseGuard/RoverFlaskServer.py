import os
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
from flask import Flask, render_template, request # , redirect, url_for, make_response
from time import sleep
import atexit

app = Flask(__name__) # set up flask server

def init():
        print "init started"

# when the root IP is selected, return rover.html page
@app.route('/')
def index():
        init()
        try:
          return render_template('roverWithservoBox.html')
        except Exception as e:
          print e
          pass

#@app.route("/<reset>")
def reset():
        GPIO.cleanup()
        print "reset"

# receive servo value
@app.route("/hor")
def hor():
        horValue = request.args.get('servolr', None)
        print "LRPos received"
        print horValue
		var = (300-int(horValue))/2
		print val
        os.system("python servocontrol.py 4 " + str(val))
        return horValue

@app.route("/ver")
def ver():
        verValue = request.args.get('servodu', None)
        print "DUPos received"
        print verValue
		val = (300-int(verValue))/2
		print val
        os.system("python servocontrol.py 2 " + str(val))
        return verValue

@app.route("/pos")
def pos():
        horValue = request.args.get('servolr', None)
        verValue = request.args.get('servodu', None)
        print "Pos received"
        print horValue + " and " + verValue
		valh = (300-int(horValue))/2
		valv = int(verValue)/2
		print str(valh) + " and " + str(valv)
	    os.system("python servocontrol.py 4 " + str(valh))
		os.system("python servocontrol.py 2 " + str(valv))
        return "OK"

# receive direction from the button press on rover.html
@app.route("/<direction>") # , method=['POST']
def move(direction):
                # Choose the direction of the request
                if direction == 'go':
                        os.system("python motorcontrol.py go")
                        print "Rover Go"
				elif direction == 'back':
                        os.system("python motorcontrol.py back")
                        print "Rover Back"
                elif direction == 'left':
                        os.system("python motorcontrol.py left")
                        print "Rover Left"
                elif direction == 'right':
                        os.system("python motorcontrol.py right")
                        print "Rover Right"
                elif direction == 'stop':
                        os.system("python motorcontrol.py stop")
                        print "Rover Stop"

                return direction

                # or
                #  response = make_response(redirect(url_for('index')))
                # return(response)

# Clean everything up when the app exits
atexit.register(reset)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=9000, debug=True)