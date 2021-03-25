import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

from lightup import lightup

leds = [24,25,8,7,12,16,20,21]

def runningLight(count,period):
    for i in range(count):
        for k in range(8): 
            lightup(leds[k], period)