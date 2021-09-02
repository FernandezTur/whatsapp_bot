For this bot to work, you will need a Twilio account (Whatsapp Sandbox), a virtual environment, and ngrok installed for the webhook.
Once ngrok is installed run: $ ngrok http 5000
Then on another console (leave ngrok running) source/activate your Virtual Environment (venv) and run the program: $ python3 whatsapp_bot.py
Leave that running too...
Then go to the Whatsapp Sandbox on Twilio and add the ngrok session's HTTPS forwarding address on the "When a message comes in" Sandbox Configuration (This is under Messaging/Settings/WhatsApp sandbox settings). Make sure to select "HTTP Post".
Append the forwarding address with the bot-app's name ("whatsapp_bot" in this case)
Here is an example of how it should look:
	https://1876-73-134-115-198.ngrok.io/whatsapp_bot
	
Don't forget to SAVE!
