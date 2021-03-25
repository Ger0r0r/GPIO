import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [24,25,8,7,12,16,20,21]


def decToBinList(decNumber):
    a = [0,0,0,0,0,0,0,0]
    for i in range(8):
        a[i] = decNumber % 2
        decNumber = decNumber // 2
    return a
