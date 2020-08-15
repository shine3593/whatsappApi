import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC27a750bcfc0119b3d89f006c3e1ab707'
auth_token = 'e1355a79f99086f4e1504ce917d3d77a'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hi bomma!',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+919398825677'
                          )

print(message.sid)
