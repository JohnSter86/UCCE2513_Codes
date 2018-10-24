import paho.mqtt.client as mqtt

broker = "127.0.0.1"
port = 1883
topic = "mypi/dht11"

def on_connect(client1, userdata, flags, rc):
    print("rc: " + str(rc))
    client1.subscribe(topic)

def on_subscribe(client1, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client1, userdata, message):
    print("Message received ", str(message.payload.decode("utf-8")))

client1 = mqtt.Client("P1")
client1.on_connect = on_connect
client1.on_sunscribe = on_subscribe
client1.on_message = on_message
client1.connect(broker, port)
client1.loop_forever()
