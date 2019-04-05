import random
from flask import Flask, request
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

    randoMSG = ['you tell me','dope','maybe','hows Cerner?','i am if you are', 'you seemed off monday']
    # Add a message
    resp.message(random.choice(randoMSG))

    return str(resp)

if __name__ == '__main__':
    app.run()
    



