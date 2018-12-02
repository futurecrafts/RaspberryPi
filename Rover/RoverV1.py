import os
import RPi.GPIO as GPIO
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
          return render_template('roverv1.html')
        except Exception as e:
          print e
          pass

#@app.route("/<reset>")
def reset():
        GPIO.cleanup()
        print "reset"

# receive direction from the button press on roverv1.html
@app.route("/<direction>") # , method=['POST']
def move(direction):
                # Choose the direction of the request
                if direction == 'go':
                        os.system("python motorcontrol_old.py go")
                        print "Rover Go"
		elif direction == 'back':
                        os.system("python motorcontrol_old.py back")
                        print "Rover Back"
                elif direction == 'left':
                        os.system("python motorcontrol_old.py left")
                        print "Rover Left"
                elif direction == 'right':
                        os.system("python motorcontrol_old.py right")
                        print "Rover Right"
                elif direction == 'stop':
                        os.system("python motorcontrol_old.py stop")
                        print "Rover Stop"

                return direction

                # or
                #  response = make_response(redirect(url_for('index')))
                # return(response)

# Clean everything up when the app exits
atexit.register(reset)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=9000, debug=True)
