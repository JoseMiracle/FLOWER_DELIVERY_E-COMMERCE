import os
from dotenv import load_dotenv
load_dotenv()
from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
account_sid = os.getenv('ACCOUNT_SID')
auth_token  = os.getenv('AUTH_TOKEN')
twilio_number = os.getenv('TWILIO_NUMBER')

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+2349157754181",
    from_=twilio_number,
    body="Hello Bright")

print(message.sid)