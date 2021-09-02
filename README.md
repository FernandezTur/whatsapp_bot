# How to write a WhatsApp bot using Flask, Twilio, and Ngrok

Follow the instructions on this [link](https://www.twilio.com/blog/build-a-whatsapp-chatbot-with-python-flask-and-twilio).

## Setup in a Nutshell...
For this bot to work, you will need to do the following:
1. Create a Twilio account (Whatsapp Sandbox)
2. Setup a virtual environment (pip install twilio flask requests)
3. Intall Ngrok (generates a temporary forwarding address for the chatbot)

After setup, follow these steps:
1. Make sure to import all the necessary packages.
2. Use the Flask framework to create a web application. In this case a chatbot service. Use "initial_setup.py" as reference for the webhook.
3. Add messages and responses management code
4. Add chatbot logic
5. Test

## How to test
1. Run: $ ngrok http 5000
	> Leave ngrok running
2. On another console/window run: $ python3 whatsapp_bot.py
	> Make sure to source/activate your Virtual Environment (venv). Leave this running too...
3. Go to the WhatsApp Sandbox on Twilio and add the ngrok session's HTTPS forwarding address
	> This address goes on the "When a message comes in" Sandbox Configuration (This is under Messaging/Settings/WhatsApp sandbox settings). Append the forwarding address with the bot-app's name ("whatsapp_bot" in this case). Here is an example of how it should look: https://1876-73-134-115-198.ngrok.io/whatsapp_bot
4. Don't forget to SAVE!
