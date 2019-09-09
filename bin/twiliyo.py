import os
from twilio.rest import Client

# alright then, keep your secrets
# Get the Twilio SID and auth token from environment variables, see startup.sh
twilio_sid = os.environ.get('TWILIO_SID')
twilio_auth = os.environ.get('TWILIO_AUTH')

# set up the Twilio client
client = Client(twilio_sid, twilio_auth)

# Prompt the user for message parameters
# TODO: Sanitize input (at least check for NANP format)

def promptUser():
    messageRecipient = raw_input("Recipient number: ")
    messageBody = raw_input("Message body: ")
    sendMessage(messageRecipient, messageBody)

def sendMessage(messageRecipient, messageBody):
    message = client.messages.create(
        body=messageBody,
        from_='+19705915361',
        to=messageRecipient
        )
    print(message.sid)

promptUser()
