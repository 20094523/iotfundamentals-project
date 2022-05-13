from sense_hat import SenseHat
sense = SenseHat()
import time
import random
import os
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACCOUNT SID"
# Your Auth Token from twilio.com/console
auth_token  = "ACCOUNT TOKEN"

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
    account_sid = "ACCOUNT SID"
    # Your Auth Token from twilio.com/console
    auth_token  = "ACCOUNT TOKEN"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="YOUR PHONE NUMBER", 
        from_="TWILIO PHONE NUMBER",
        body="Movement detected at door. Check website: http://YOURPI'SNAME.local/")
    time.sleep(5)
