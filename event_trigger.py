import RPi.GPIO as GPIO
from ubidots import ApiClient
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT, initial=0) #use GPIO22

api = ApiClient(token='authentication_token')   #change your token here
my_switch = api.get_variable('variable_id')     #change your variable ID here

while(1):
    try:
        status = my_switch.get_values(1)
        if status[0]['value']:
            GPIO.output(22, 1)
            print("status: %d" % status[0]['value'])
        else:
            GPIO.output(22,0)
            print("status: %d" % status[0]['value'])
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
