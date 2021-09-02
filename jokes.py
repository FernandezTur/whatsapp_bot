# Concept for a dad joke telling bot
import random

jokes = open("dad_jokes.txt").readlines()
more_jokes = True
prompt = "Hello friend! Would you like to hear a joke?(YES/NO)"
response = input(prompt)

while more_jokes:
	if 'yes' in response.lower():
		joke = random.choice(jokes)
		print(joke)
		prompt = "\nReply again to get another joke: "
		response = input(prompt)
		more_jokes = True
	
	else:
		print('Too bad...')
		more_jokes = False
else:
	print("\nHope you enjoyed all the jokes. Good-bye!")
