import random

# Some useful variables
guesses = []
maxfails = 7
fails = 0
endGame = "s"
# A list of words that
potential_words = ["python", "chicago", "train", "sphinx", "labyrinth", "java", "awkward", "bagpipes", "banjo","bungler","dwarves","skyscraper","laptop","bus","marker","amplifier", "code","lunch"]
word = random.choice(potential_words)
triesLeftString = "You have " + str(maxfails - fails) + " tries left!"
def triesLeft():
    if fails == 7:
        print("You lost, the word was " + word)
    elif fails == 6:
        print("You have 1 try left!")
    else:
        print("You have " + str(maxfails - fails) + " tries left!")
#print("Type stop to end the game.")

# Use to test your code:
#print(word)

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
current_word = [] # TIP: the number of letters should match the word
for i in range(len(word)):
    current_word.append("_")
print(' '.join(current_word))
#if input("stop"):
    #exit()

while fails < maxfails:
    guess = input("Guess a letter: ")
    print()
    guess = guess.lower()

 #check if the guess is valid: Is it one letter? Have they already guessed it?
    if len(guess) > 1:
        print("Only guess one letter")
        fails += 1
        triesLeft()
        print()

    elif guess.isdigit():
        print("Only guess letters!")
        fails += 1
        triesLeft()
        print()

    elif guess in guesses:
        print("You've already guessed that, try again.")
        #guesses.append(guess)
        fails += 1
        triesLeft()
        print()

    elif guess not in word:
        print("Try again!")
        fails += 1
        #guesses.append(guess)
        triesLeft()
        print()

    else:
        for i in range(len(word)):
            if guess == word[i]:
                current_word[i] = word[i]
                print()
                #guesses.append(guess)
    guesses.append(guess)
    print("You have guessed the letters: " + ', '.join(guesses))
    print(' '.join(current_word))
    print()
    if "_" not in current_word:# REVIEW: 
        print("You won!")
        print()
        maxfails = fails

    if fails == 7:
        print("You lost!")
        print("The word was: " + word)
