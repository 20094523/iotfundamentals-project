from sense_hat import SenseHat
sense = SenseHat()
from paho.mqtt import client as mqtt_client
import time
import random
import os
from twilio.rest import Client

broker = 'broker.emqx.io'
port = 1883
topic = "/python/mqtt"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'username'
password = 'password'

while True:
  o = sense.get_orientation()
  roll = o["roll"]
  trueroll=round(roll)
  
  time.sleep(.5)
  p = sense.get_orientation()
  roll2 = p["roll"]
  trueroll2=round(roll2)
  
  print("Roll1= " + str(trueroll) + " " + "Roll2= " + str(trueroll2))
  time.sleep(.1)

##
  if trueroll>=trueroll2 +20 or trueroll2>=trueroll +20:
    # Your Account SID from twilio.com/console
    account_sid = "AC8861bc46213d6c73aed5cfc4cffbed89"
    # Your Auth Token from twilio.com/console
    auth_token  = "a859e7383a475c7951af57fb6971c061"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+353867967343", 
        from_="+19705195868",
        body="Movement detected at door. Check website: http://streaming.local/")
    time.sleep(5)
