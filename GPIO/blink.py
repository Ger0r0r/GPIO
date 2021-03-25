import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def blink(ledNumber,blinkCount,blinkPeriod):
    for i in range(blinkCount):
        GPIO.output(ledNumber,1)
        time.sleep(blinkPeriod)
        GPIO.output(ledNumber,0)
        time.sleep(blinkPeriod)
