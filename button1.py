from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT, initial=0)                 #use GPIO17 as output
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)   #use GPIO10 as input

while True:
    try:
        if (GPIO.input(10) == 0):   #if switch is pressed
            GPIO.output(17, 1)       #turn on red LED
        else:
            GPIO.output(17, 0)       #turn off red LED
        sleep(.2)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
