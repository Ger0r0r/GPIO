import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [25,24,21,20,16,12,7,8]

GPIO.setup(leds,GPIO.OUT)

GPIO.output(24,1) #индикатор рабочести

while True:
    GPIO.output(21,1)
    time.sleep(0.1)
    GPIO.output(20,1)
    time.sleep(0.1)
    GPIO.output(16,1)
    time.sleep(0.1)
    GPIO.output(12,1)
    time.sleep(0.1)
    GPIO.output(7,1)
    time.sleep(0.1)
    GPIO.output(8,1)
    time.sleep(0.1)

    GPIO.output(21,0)
    time.sleep(0.1)
    GPIO.output(20,0)
    time.sleep(0.1)
    GPIO.output(16,0)
    time.sleep(0.1)
    GPIO.output(12,0)
    time.sleep(0.1)
    GPIO.output(7,0)
    time.sleep(0.1)
    GPIO.output(8,0)
    time.sleep(0.1)
    

#GPIO.output(leds,0)
#GPIO.cleanup()