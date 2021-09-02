import requests
import json
from twilio.twiml.messaging_response import MessagingResponse

#incoming_msg = requests.values.get('Body', '')
prompt = 'Hello friend! Would you like to hear a joke?'
print(promt)
resp = MessagingResponse()
msg = resp.message()
responded = False
msg = input()

if ('Hi' in incoming_msg) or ('Hey' in incoming_msg) or ('Hello' in incoming_msg) or ('Menu' in incoming
_msg):
	text = f'Hello 🙋🏽‍♂, \nThis is a comedy bot. Say YES if you want to hear a joke and NO if you d
o not.'
	msg.body(text)
	responded = True

if 'YES' in incoming_msg:
#		joke = "I am afraid for the calendar. Its days are numbered.\n"
		#print(joke)
	print("knock knock!")
else:
	print("Too bad you lack sense of humor. Good bye!")
