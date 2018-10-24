import Adafruit_DHT
import paho.mqtt.client as mqtt
from time import sleep

broker = "127.0.0.1"
port = 1883
topic = "mypi/dht11"
interval = 5.0  #interval in seconds

sensor = Adafruit_DHT.DHT11
pin = 18

def on_connect(client1, userdata, flags, rc):
    print("rc: " + str(rc))

def on_publish(client,userdata,result):
    print('Temp={0:0.1f}*C'.format(temperature))
    pass

client1 = mqtt.Client("P0")
client1.username_pw_set(username="iotuser",password="abc123")
client1.on_connect = on_connect
client1.on_publish = on_publish 
client1.connect(broker, port)
client1.loop_start()
while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        client1.publish(topic, str(temperature))
    sleep(interval)
client1.loop_stop()
