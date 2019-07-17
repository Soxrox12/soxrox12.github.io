#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
tries = 3
# For Testing: print(aRandomNumber)
while tries > 0:
	guess = input("Guess a number between 1 and 20 (inclusive): ")
	if not guess.isnumeric(): # checks if a string is only digits 0 to 9
		print("That's not a positive whole number, try again!")
	else:
		guess = int(guess) # converts a string to an integer
		if(guess == aRandomNumber):
			print("You won!")
			break
		elif(guess > aRandomNumber):
			tries -= 1
			if(tries == 0):
				print("You lost!")
				break
			else:
				print("Nope! Try guessing lower next time!")
				continue
		else:
			tries -= 1
			if(tries == 0):
				print("You lost!")
				break
			else:
				print("Nope! Try guessing higher next time!")
				continue
