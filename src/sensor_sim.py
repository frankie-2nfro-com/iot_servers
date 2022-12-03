import time
import paho.mqtt.client as mqtt
import json
import sys
import random
import time

print("Testing sending message to mqtt")

def on_connect(client, userdata, flags, rc):
    # This will be called once the client connects
    print(f"Connected with result code {rc}")

def on_publish(client,userdata,result):             #create function for callback
    print("data published\n")

client = mqtt.Client("mqtt-iot1-sensor-sim") # client ID "mqtt-test"
client.on_connect = on_connect
client.on_publish = on_publish 
client.username_pw_set("frankiesiu", "frankie01")
client.connect("localhost", 1883)

counter = 0
while True:
    s = random.random()
    if (counter%2)==0:
        ret = client.publish("iot1", 'MASK|12345' + str(s) + '[MASK]77890')
    ret = client.publish("iot1_result", '{"score": ' + str(s) + '}') 
    time.sleep(5)
    counter = counter + 1




