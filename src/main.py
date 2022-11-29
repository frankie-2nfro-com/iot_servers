import sys
import time
import paho.mqtt.client as mqtt
from transformers import pipeline 
from transformers import AutoTokenizer, AutoModelForMaskedLM

print("Hello docker single stage image.....ver 1.0.8", sys.argv)

# load model
model_name = "bert-base-chinese"
print("Loading model: {}".format(model_name))
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForMaskedLM.from_pretrained(model_name)
unmasker = pipeline('fill-mask', model=model_name)
print("Loaded")
print(model)

# should be get argv to know the mqtt channel name
# Loop the program after loading the model
# When subscription message found - handle it and get model resutl
# Publish result to the mqtt

def on_connect(client, userdata, flags, rc):
    # This will be called once the client connects
    print(f"Connected with result code {rc}")
    # Subscribe here!
    client.subscribe("iot1")

def on_message(client, userdata, msg):
    print(f"Message received [{msg.topic}]: {msg.payload}")
    command = str(msg.payload, encoding="utf-8")
    if "|" in command:
        command_details = command.split("|")
        if len(command_details) >= 2:
            cmd = command_details[0]
            param1 = command_details[1]
            
            if cmd == "MASK":
                # call model with parameter and get the result
                output = unmasker(param1)   # "東京是[MASK]国的首都。"
                print(output)

                # publish result to the mqtt
                ret= client.publish("iot1_result", output) 
            else:
                print("Command: {}".format(cmd))
                print("Parameter 1: {}".format(param1))

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass



client = mqtt.Client("mqtt-test") # client ID "mqtt-test"
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish 
client.username_pw_set("frankiesiu", "frankie01")
client.connect('mosquitto', 1883)
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


