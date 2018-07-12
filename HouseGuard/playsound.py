
#!/usr/bin/env python

"""playsound.py: Trigger script for playing sound."""

__author__ = "FutureCrafts"
__email__ = "futurecrafts.yb@gmail.com"

import pygame

#import RPi.GPIO as GPIO
#import time

#GPIO Mode (BOARD / BCM)
#GPIO.setmode(GPIO.BCM)

#set GPIO Pins
#GPIO_TRIGGER = 18
#GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
#GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
#GPIO.setup(GPIO_ECHO, GPIO.IN)

# User pygame for sounds

pygame.mixer.pre_init(44100, -16, 12, 512)
pygame.init()

kick = pygame.mixer.Sound('samples/kick.wav')
kick.set_volume(.65);
snare = pygame.mixer.Sound('samples/snare.wav')
snare.set_volume(.65);
openhh = pygame.mixer.Sound('samples/open.wav')
openhh.set_volume(.65);
closedhh = pygame.mixer.Sound('samples/closed.wav')
closedhh.set_volume(.65);
clap = pygame.mixer.Sound('samples/clap.wav')
clap.set_volume(.65);
cymbal = pygame.mixer.Sound('samples/cymbal.wav')
cymbal.set_volume(.65);

while True:
  
	kick.play()
  print( 'kick was just played')
	snare.play()
  print( 'snare was just played')
	openhh.play()
  print( 'openhh was just played')
	closedhh.play()
  print( 'closedhh was just played')
	clap.play()
  print( 'clap was just played')
	cymbal.play()
  print( 'cymbal was just played')
  
#  def distance():
    # set Trigger to HIGH
#    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
#    time.sleep(0.00001)
 #   GPIO.output(GPIO_TRIGGER, False)
 
#    StartTime = time.time()
#    StopTime = time.time()
 
    # save StartTime
 #   while GPIO.input(GPIO_ECHO) == 0:
 #       StartTime = time.time()
 
    # save time of arrival
  #  while GPIO.input(GPIO_ECHO) == 1:
  #      StopTime = time.time()
 
    # time difference between start and arrival
 #   TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
 #   distance = (TimeElapsed * 34300) / 2
 
 #   return distance
 
#if __name__ == '__main__':
 #   try:
 #       while True:
  #          dist = distance()
  #          print ("Measured Distance = %.1f cm" % dist)
   #         time.sleep(1)
 
        # Reset by pressing CTRL + C
  #  except KeyboardInterrupt:
  #      print("Measurement stopped by User")
   #     GPIO.cleanup()
