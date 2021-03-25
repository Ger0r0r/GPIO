import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

from decToBinList import decToBinList

leds = [24,25,8,7,12,16,20,21]

GPIO.setup(leds,GPIO.OUT)


def lightNumber(Number):
    a = decToBinList(Number)

    for i in range(8):
        GPIO.output(leds[i],a[i])
