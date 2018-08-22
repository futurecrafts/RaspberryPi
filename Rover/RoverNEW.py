# need to install Flask (sudo pip install flask), ServoBlaster
"""
Auto Start Up Upon Login

First thing you need to do is set up the Pi to boot straight to the CLI and log in without prompt. To do this, go to the Raspberry Pi Configuration tool (raspi-config) and tick the box to auto log in as the user pi.

Now finally you can go ahead and put the commands that need to be executed in the .bashrc file.

sudo nano ~/.bashrc

In here, go to the bottom of the file and add this line:

sudo service motion start & python location_where_you_put_the_code_/WebControlledRobot/app.py

Now whenever you log in, you will be asked for your sudo password and it will kick into action. The quickest way I do this is using ssh on my phone or computer.

Concerning ServoBlaster: (http://www.instructables.com/id/IoT-Raspberry-Pi-Video-Streamer-and-PanTilt-Camera/)
Servo mapping:
     0 on P1-7           GPIO-4
     1 on P1-11          GPIO-17
     2 on P1-12          GPIO-18
     3 on P1-13          GPIO-27
     4 on P1-15          GPIO-22
     5 on P1-16          GPIO-23
     6 on P1-18          GPIO-24
     7 on P1-22          GPIO-25
	 
	 We will only need 2 servos, so we must restrict the pins to be used.
	GPIO.18 (P1-12) will be used for Servo1
    GPIO.23 (P1-16) will be used for Servo2
	
	To define the pins to be used, the bellow parameters must be used:
	sudo ./servod --p1pins=12,16
	
	Running the above command, the monitor will now show in its lower part:
		Using P1 pins: 12,16
		Servo mapping:
		0 on P1-12 GPIO-18
		1 on P1-16 GPIO-23
		
	Also note that if you reboot the RPi, the configuration will l be lost, so. it's important to include the last command at /etc/rc.local

	sudo nano /etc/rc.local
		...

		cd /home/pi/PiBits/ServoBlaster/user

		sudo ./servod --p1pins=12,16

		cd 
	
	Also it is important change the script bellow:

	sudo nano /etc/init.d/servoblaster

		...

		case "$1" in
		start)

		/usr/local/sbin/servod $OPTS >/dev/null

		change to:

		/usr/local/sbin/servod --p1pins=12,16 $OPTS >/dev/null

		...
	
	now reboot
	
	Note that at this point ServoBlaster will recognize only two servos:

	servo 0 ==> p1-12

	servo 1==> P1-16

	The echo command can be done on any one of the bellow formats, with same result:

	echo P1-12=40% >/dev/servoblaster

	echo P1-16=60% >/dev/servoblaster

		or

	echo 0=40% >/dev/servoblaster

	echo 1=60% >/dev/servoblaster
	
	
	# 1000us/2000us is normally the extremes and 1500us is centered.
	# Most servos have a range from about 1000us to about 2000us.
"""

from flask import Flask, render_template #, request, redirect, url_for, make_response
#import Servoblast as Servo
from pythonSB import *
from time import sleep
import atexit

app = Flask(__name__) # set up flask server

#sc = Servo.ServoController()
#LServo = 1
#RServo = 2
LServoNum = 0
RServoNum = 1

# when the root IP is selected, return rover.html page
@app.route('/')
def index():
		try:
			return render_template('rover.html')
		except Exception as e:
				print e
				pass
				
#@app.route("/<reset>")
def reset():
		servo_set(LServoNum, "1340us", "servo")
		servo_set(RServoNum, "1340us", "servo")
		#sc.setAngle(LServo, 0)
		#sc.setAngle(RServo, 0)
				
# receive direction from the button press on rover.html
@app.route("/<direction>") # , method=['POST']
def move(direction):
		# Choose the direction of the request
		if direction == 'go':
			servo_set(LServoNum, "1440us", "servo")
			#servo_set_angle(LServo, 100)
			servo_set(RServoNum, "1240us", "servo")
			#sleep(2)
			#print "Rover Go"
		elif direction == 'back':
			servo_set(LServoNum, "1240us", "servo")
			servo_set(RServoNum, "1440us", "servo")
			#sleep(2)
			#print "Rover Back"
		elif direction == 'left':
			servo_set(LServoNum, "1340us", "servo")
			servo_set(RServoNum, "1240us", "servo")
			#sleep(2)
			#print "Rover Left"
		elif direction == 'right':
			servo_set(LServoNum, "1440us", "servo")
			servo_set(RServoNum, "1340us", "servo")
			#sleep(2)
			#print "Rover Right"
		elif direction == 'stop':
			servo_set(LServoNum, "1340us", "servo")
			servo_set(RServoNum, "1340us", "servo")
			#sleep(2)
			#print "Rover Stop"
			
		return direction
		
		# or 
		#  response = make_response(redirect(url_for('index')))
		# return(response)
		
# Clean everything up when the app exits
atexit.register(reset)
		
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=9000, debug=True)

