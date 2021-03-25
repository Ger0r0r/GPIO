import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

from lightup import lightup

def PWM(ledNumber,period):
    pp = period / 256
    for i in range(256):
        b = (256 - i)/256 * pp
        a = i/256 * pp
        print(a)
        lightup(ledNumber,a)
        time.sleep(b)

    for i in range(256):
        b = (256 - i)/256 * pp
        a = i/256 * pp
        print(b)
        lightup(ledNumber,b)
        time.sleep(a)    

        
        

    



