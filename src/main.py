import sys

print("Hello docker single stage image.....ver 1.0.2", sys.argv)

# should be get argv to know the mqtt channel name
# Loop the program after loading the model
# When subscription message found - handle it and get model resutl
# Publish result to the mqtt



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


"""
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    # This will be called once the client connects
    print(f"Connected with result code {rc}")
    # Subscribe here!
    client.subscribe("my-topic")

def on_message(client, userdata, msg):
    print(f"Message received [{msg.topic}]: {msg.payload}")
    print(userdata)

client = mqtt.Client("mqtt-test") # client ID "mqtt-test"
client.on_connect = on_connect
client.on_message = on_message
#client.username_pw_set("myusername", "aeNg8aibai0oiloo7xiad1iaju1uch")
client.connect('192.168.31.153', 1883)
client.loop_forever()  # Start networking daemon
"""