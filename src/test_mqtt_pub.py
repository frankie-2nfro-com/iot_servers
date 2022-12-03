import time
import paho.mqtt.client as mqtt
import json
import sys

print("Testing sending message to mqtt")

def on_connect(client, userdata, flags, rc):
    # This will be called once the client connects
    print(f"Connected with result code {rc}")

def on_publish(client,userdata,result):             #create function for callback
    print("data published\n")

client = mqtt.Client("mqtt-hb-test") # client ID "mqtt-test"
client.on_connect = on_connect
client.on_publish = on_publish 
client.username_pw_set("frankiesiu", "frankie01")
client.connect(sys.argv[1], 1883)
ret = client.publish(sys.argv[2], sys.argv[3]) 




