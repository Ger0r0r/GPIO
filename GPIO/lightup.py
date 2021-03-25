import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def lightup(ledNumber,period):
    GPIO.output(ledNumber,1)
    time.sleep(period)
    GPIO.output(ledNumber,0)