import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    
    client.subscribe("jiangmy/pong")
    client.message_callback_add("jiangmy/pong", on_message_pong)


def on_message_pong(client, userdata, message):
    time.sleep(1)
    count = (int) (message.payload.decode())
    client.publish("jiangmy/ping", count +1)

if __name__ == '__main__':
    #create a client object
    client = mqtt.Client()
    
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
    
    client.connect(host="172.20.10.13", port=1883, keepalive=60)

    """ask paho-mqtt to spawn a separate thread to handle
    incoming and outgoing mqtt messages."""
    time.sleep(1)

    count = 0
    client.publish("jiangmy/ping", count)

    client.loop_forever()













