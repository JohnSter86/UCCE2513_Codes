import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT, initial=0) #use GPIO17 (red LED)

while True:
    try:
        GPIO.output(17, 1)   #turn on red LED
        time.sleep(1)       #wait 1 second
        GPIO.output(17, 0)   #turn off red LED
        time.sleep(1)       #wait 1 second
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()

