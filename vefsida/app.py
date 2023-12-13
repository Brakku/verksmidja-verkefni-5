


from flask import Flask, request, jsonify,render_template
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap
import time
import random
import json
import requests
global data
data={'payload':"0"}
cpu=0

app = Flask(__name__)

app.config['MQTT_BROKER_URL'] = '10.201.48.99'
#app.config['MQTT_BROKER_URL'] = '192.168.186.211'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_KEEPALIVE'] = 5  # Set KeepAlive time in seconds
app.config['MQTT_TLS_ENABLED'] = False  # If your server supports TLS, set it True
topic = '/flask/mqtt'

mqtt_client = Mqtt(app)

@mqtt_client.on_connect()
def handle_connect(client, userdata, flags, rc):
   if rc == 0:
       print('Connected successfully')
       mqtt_client.subscribe(topic) # subscribe topic
   else:
       print('Bad connection. Code:', rc)

@mqtt_client.on_message()
def handle_mqtt_message(client, userdata, message):
    
    msg = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    global data
    data=msg
    print('Received message on topic: {topic} with payload: {payload}'.format(**msg))
    requests.post('https://maker.ifttt.com/trigger/notifacation/with/key/pLUxXzpbKRDziVWDsXXp9rZe-6kH56_4dZtrHYjxl4w')
    global done
    done =False
    handle_publish(1,1,int(data['payload']))
        

        

@mqtt_client.on_publish()
def handle_publish(a,d,datat):
    global done
    
    if datat >= 50 and done==False:
        Mqtt.publish(mqtt_client,'water/watering1',"water the plants"+str(datat))
        print("sent")
        
        datat=0
        done=True
    else:
        pass
        
    
    
    
    


@app.route('/')
def index():
    global data
    
    return render_template('index.html',data=data,datai=int(data['payload']))



@app.context_processor
def clever_function():
    return dict(myexample='This is an example')




if __name__ == '__main__':
   app.run(host='127.0.0.1', port=5000,debug=True)




