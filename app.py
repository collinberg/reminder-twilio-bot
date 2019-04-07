import random
from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/dope')
def dope():
	return 'Dopeness!'

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    randoMSG = ['you tell me','Well im not sam','maybe','thats unprofessional','i am if you are', 'Where were you October 07']
    # Add a message
    resp.message(random.choice(randoMSG))

    return str(resp)

@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    resp.say("What happened on October 7th at the Egyptian Royalty House", voice='alice')

    return str(resp)

if __name__ == '__main__':
    app.run()
    



