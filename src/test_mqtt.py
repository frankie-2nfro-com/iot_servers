import time
import paho.mqtt.client as mqtt
import json

print("Testing connecting to mqtt")

def on_connect(client, userdata, flags, rc):
    # This will be called once the client connects
    print(f"Connected with result code {rc}")
    ret = client.publish("heartbeat", "after connected, first test pusblish...") 

def on_message(client, userdata, msg):
    print(f"Message received [{msg.topic}]: {msg.payload}")

def on_publish(client,userdata,result):             #create function for callback
    print("data published\n")

client = mqtt.Client("mqtt-test") # client ID "mqtt-test"
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish 
client.username_pw_set("frankiesiu", "frankie01")
client.connect('mosquitto', 1883)
client.subscribe("heartbeat")

client.loop_forever()  # Start networking daemon








# mosquitto_pub -h 127.0.0.1 -m "test test" -t "iot1" -u frankiesiu -P frankie01
# mosquitto_sub -h 127.0.0.1 -t "iot1" -u frankiesiu -P frankie01

"""
import paho.mqtt.client as paho

broker="192.168.31.153"
port=1883

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass

client1= paho.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)                                 #establish connection
ret= client1.publish("my-topic", "onxx")   
"""


