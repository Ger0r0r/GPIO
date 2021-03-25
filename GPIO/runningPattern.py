import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

from decToBinList import decToBinList
from lightNumber import lightNumber

leds = [24,25,8,7,12,16,20,21]

GPIO.setup(leds,GPIO.OUT)

def runningPattern(pattern,direction):
    for i in range(64):
        lightNumber(pattern)
        time.sleep(0.1)
        b = pattern % 2
        if direction > 0:
            b = pattern % 2
            pattern = pattern >> 1
            pattern = pattern + b * 128
        else:
            b = pattern // 128
            pattern = pattern % 128
            pattern = pattern * 2 + b



