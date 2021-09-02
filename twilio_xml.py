from twilio.twiml.messaging_response import MessagingResponse

resp = MessagingResponse()
msg = resp.message()
msg.body('this is the response text')
msg.media('https://example.com/path/image.jpg')
