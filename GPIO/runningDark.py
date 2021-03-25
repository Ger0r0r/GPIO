import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [24,25,8,7,12,16,20,21]

def runningDark(count,period):
    GPIO.output(leds,1)
    for i in range(count):
        for k in range(8):
            GPIO.output(leds[k],0)
            time.sleep(period)
            GPIO.output(leds[k],1)