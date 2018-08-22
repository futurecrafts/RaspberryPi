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
		Using P1 pins: 11,16
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
"""

from flask import Flask, render_template #, request, redirect, url_for, make_response
import Servoblast as Servo
from time import sleep

app = Flask(__name__) # set up flask server

sc = Servo.ServoController()
LServo = 1
RServo = 2

# when the root IP is selected, return rover.html page
@app.route('/')
def index():
		try:
			return render_template('rover.html')
		except Exception as e:
				print e
				pass
				
# receive direction from the button press on rover.html
@app.route("/<direction>", method=['POST'])
def move(direction):
		# Choose the direction of the request
		if direction == 'go':
			sc.setAngle(LServo, 45)
			sc.setAngle(RServo, 45)
			sleep(2)
			#print "Rover Go"
		elif direction == 'back':
			sc.setAngle(LServo, 45)
			sc.setAngle(RServo, 45)
			sleep(2)
			#print "Rover Back"
		elif direction == 'left':
			sc.setAngle(LServo, 45)
			sc.setAngle(RServo, 45)
			sleep(2)
			#print "Rover Left"
		elif direction == 'right':
			sc.setAngle(LServo, 45)
			sc.setAngle(RServo, 45)
			sleep(2)
			#print "Rover Right"
		elif direction == 'stop':
			sc.setAngle(LServo, 45)
			sc.setAngle(RServo, 45)
			sleep(2)
			#print "Rover Stop"
			
		return direction
		
		# or 
		#  response = make_response(redirect(url_for('index')))
		# return(response)
		
@app.route("/<reset>")
def reset():
		sc.setAngle(LServo, 0)
		sc.setAngle(RServo, 0)
		
if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=8000)

