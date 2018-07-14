"""playsound_with_pir.py: Trigger script for playing sound with PIR sensor."""

__author__ = "FutureCrafts"
__email__ = "futurecrafts.yb@gmail.com"

import pygame

import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
PIR = 20

print "Starting PIR Sensor..."
 
#set GPIO direction (IN / OUT)
GPIO.setup(PIR, GPIO.IN)

# User pygame for sounds

pygame.mixer.pre_init(44100, -16, 12, 512)
pygame.init()

kick = pygame.mixer.Sound('kick.wav')
kick.set_volume(.65);
snare = pygame.mixer.Sound('snare.wav')
snare.set_volume(.65);
openhh = pygame.mixer.Sound('open.wav')
openhh.set_volume(.65);
closedhh = pygame.mixer.Sound('closed.wav')
closedhh.set_volume(.65);
clap = pygame.mixer.Sound('clap.wav')
clap.set_volume(.65);
cymbal = pygame.mixer.Sound('cymbal.wav')
cymbal.set_volume(.65);

try:
    time.sleep(2)
    while True:
        if GPIO.input(PIR):
            print "Motion Detected..."
            cymbal.play()
            time.sleep(2)
        time.sleep(0.1)
        
except:
    GPIO.cleanup()
