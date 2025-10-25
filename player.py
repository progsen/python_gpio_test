## apt-install python3-pygame
## apt-get install python3-rpi.gpio

import RPi.GPIO as GPIO
import time
import pygame
import os

#GPIO.setmode(GPIO.BCM) # Use BCM numbering
GPIO.setmode(GPIO.BOARD) # Use physical board numbering

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

path = "./music"
dir_list = os.listdir(path)

files = os.listdir(path)
current = 0;
running=True;

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(files[current])
pygame.mixer.music.play()

def next():

    if pygame.mixer.music.get_busy() == True:
        print("stop music")
        pygame.mixer.music.stop()
    current++
    if current > len(files) :
        current=0
    pygame.mixer.music.load(files[current])
    pygame.mixer.music.play()
    
while running: 
    if GPIO.input(10) == GPIO.HIGH:
        print("Button was pushed!")
        next()

    if pygame.mixer.music.get_busy() == False:
        print("music done")
        next()
    time.sleep(0.033)

GPIO.cleanup()
