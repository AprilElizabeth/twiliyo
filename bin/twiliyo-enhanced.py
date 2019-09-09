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

messageRecipient = (input"Recipient number: ")
messageBody = input("Message body: ")

def validateNumber(messageRecipient)
    try:
        response = client.lookups.phone_numbers(messageRecipient).fetch(type="carrier")
        return (client.lookups.phone_numbers(
    except TwilioRestException as e:
        if e.code == 20404:
            raise 
        else:
            raise e

def sendMessage()
    message = client.messages.create(
        body=messageBody,
        from_='+19705915361',
        to='+19703104734'
        )
    print(message.sid)

