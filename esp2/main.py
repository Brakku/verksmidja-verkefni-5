'''
from machine import Pin
from time import sleep

# ESP32 GPIO 26
relay = Pin(13, Pin.OUT)

# ESP8266 GPIO 5
#relay = Pin(5, Pin.OUT)

while True:
  # RELAY ON
  relay.value(0)
  sleep(2)
  print("on")
  # RELAY OFF
  relay.value(1)
  sleep(2)
  print("off")
'''



import random
from machine import Pin
from time import sleep
import math

def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'notification' and msg == b'received':
    print('ESP received hello message')

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()




try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()



while True:
  try:
    client.check_msg()
    if (time.time() - last_message) > message_interval:
      sinne=random.randint(1,100)
      
      msg = b'%d' % sinne
      client.publish(topic_pub, msg)
      last_message = time.time()
      print(sinne)
      
  except OSError as e:
    restart_and_reconnect()
    


"""

import dht
import machine
sleep(0.1)
d = dht.DHT11(machine.Pin(14))
sleep(5)
d.temperature()
    
d.humidity()
d.measure()
while True:
    sleep(0.1)
    
    
    d.temperature()
    
    d.humidity()
    
    print("done")
"""







