# Complete project details at https://RandomNerdTutorials.com

import time
from umqtt.simple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

ssid = 'TskoliVESM'
password = 'Fallegurhestur'

#ssid = 'Galaxy S221DC8'
#password = '00000000'


mqtt_server = '10.201.48.99'
#mqtt_server = '192.168.186.211'



client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'notificationxy5'
topic_pub = '/flask/mqtt'

last_message = 0
message_interval = 3
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
