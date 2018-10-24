import Adafruit_DHT
from ubidots import ApiClient
from time import sleep

sensor = Adafruit_DHT.DHT11
pin = 18

api = ApiClient(token='authentication_token') #change your token here
my_temp = api.get_variable('variable_id')     #change your variable ID here

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        new_temp = my_temp.save_value({'value': temperature})
    else:
        print('Failed to get reading. Try again!')
    sleep(5)
