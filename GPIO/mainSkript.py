import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [24,25,8,7,12,16,20,21]

GPIO.setup(leds,GPIO.OUT)

from lightup import lightup
from blink import blink
from runningLight import runningLight
from runningDark import runningDark
from decToBinList import decToBinList
from lightNumber import lightNumber
from runningPattern import runningPattern
from PWM import PWM

time.sleep(1)

#lightup(leds[3], 4)

#blink(leds[5],10,0.1)

#runningLight(10,0.1)

#runningDark(10,0.1)

#lightNumber(177)

#runningPattern(5,0)

PWM(leds[0],1)
PWM(leds[0],1)
PWM(leds[0],1)
PWM(leds[0],1)
PWM(leds[0],1)

#time.sleep(2)

GPIO.output(leds,0)
GPIO.cleanup()