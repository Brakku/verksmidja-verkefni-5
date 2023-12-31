# Complete project details at https://RandomNerdTutorials.com

from machine import Pin
from time import sleep
relay = Pin(13, Pin.OUT)

def sub_cb(topic, msg):
  print((topic, msg))

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
    new_message = client.check_msg()
    if new_message != 'None':
      #client.publish(topic_pub, b'received')
      if str(new_message) != 'None':
          relay.value(1)
          sleep(0.6)
          print("off")
          
          # RELAY OFF
          relay.value(0)
          sleep(0.6)
          print("on")
          
    time.sleep(1)
  except OSError as e:
    restart_and_reconnect()