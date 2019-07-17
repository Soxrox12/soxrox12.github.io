import time
import random
# --- Define your functions below! ---
def intro():
    print("Hey, I'm a chatbot. Let's get started!")
    print("Type 'exit' at any time to exit.")

def greeting():
    print("Hello! What's your name")
    name = input(" ")
    print("Hello, " + name)
def tell_a_joke():
    jokes = ["What is a pirate's favorite food? Ships and dip!", "I hate Russian dolls, they're so full of themselves.",
    "PMS jokes are not funny or appropriate. Period!", "As I watched the dog chasing his tail I thought 'Dogs are easily amused', then I realized I was watching the dog chasing his tail.",
    "What do you call a fish without an eye? A FSH", "What's blue and white and sits on the toilet? A policeman doing his duty! (Courtesy of my 6-year-old brother)"]
    joke = random.choice(jokes)
    print(joke)
def weather():
    print("Today it is 79 degrees Fahrenheit and partly cloudy.")
def rps_winner():
    user_hand = input("Type 'rock', 'paper', or 'scissors' to play: ")
    cpu_hands = ['rock', 'paper', 'scissors']
    cpu = random.choice(cpu_hands)
    choices = print('You chose ' + user_hand + ' and I chose ' + cpu + '.')
    i_win = "I win. Try again!"
    you_win = "You win! Congratulations!"
    tie = "It's a tie!"
    try_again = "Check your spelling"
    if cpu == user_hand:
        print(choices)
        print(tie)
    elif cpu == 'rock' and (user_hand in cpu_hands) :
        print(choices)
        if user_hand == 'paper':
            print(you_win)
        elif user_hand == 'scissors':
            print(i_win)
        else:
            print(try_again)
    elif cpu == 'paper' and (user_hand in cpu_hands):
        print(choices)
        if user_hand == 'rock':
            print(i_win)
        elif user_hand == 'scissors':
            print(you_win)
        else:
            print(try_again)
    elif cpu == 'scissors' and (user_hand in cpu_hands):
        print(choices)
        if user_hand == 'rock':
            print(you_win)
        elif user_hand == 'paper':
            print(i_win)
        else:
            print(try_again)
    else:
        print(try_again)
        rock_paper_scissors()

def rock_paper_scissors():
    rps_winner()





    '''user_hand = input("Type 'rock', 'paper', or 'scissors' to play: ")
    cpu_hands = ['rock', 'paper', 'scissors']
    cpu = random.choice(cpu_hands)
    if cpu == 'rock' and (user_hand in cpu_hands) :
        print('You chose ' + user_hand + ' and I chose ' + cpu + '.')
        if user_hand == 'rock':
            print('We tied!')
        elif user_hand == 'paper':
            print('You win!')
        else:
            print('I win!')
    elif cpu == 'paper' and (user_hand in cpu_hands):
        print('You chose ' + user_hand + ' and I chose ' + cpu + '.')
        if user_hand == 'rock':
            print('I win!')
        elif user_hand == 'paper':
            print('We tied!')
        else:
            print('You win!')
    elif cpu == 'scissors' and (user_hand in cpu_hands):
        print('You chose ' + user_hand + ' and I chose ' + cpu + '.')
        if user_hand == 'rock':
            print('You win!')
        elif user_hand == 'paper':
            print('I win!')
        else:
            print('You win!')
    else:
        print("Did you type 'rock', 'paper', or 'scissors'? Try again")'''
def haiku():
    fiveSyllables = ["Imagination","Nationalism","Anticipation", "Emotionally,"]
    fiveSyllables2 = ["Oh, give me a break", "The truth is out there", "We are not alone", "Old habits die hard", "Practice makes perfect"]
    sevenSyllables = ["All the very best to you", "Curiosity is good", "Learn the art of listening","I like to cook spaghetti","Oxygen is poisonous", "It was the best of times, NOT", "The story ends with a kiss"]

    randomFiveSyllables1 = random.choice(fiveSyllables)
    randomFiveSyllables2 = random.choice(fiveSyllables)
    randomSevenSyllables = random.choice(sevenSyllables)

    print("Here is your haiku:")
    print(randomFiveSyllables1)
    print(randomSevenSyllables)
    print(randomFiveSyllables2)
    print("")
def knock_knock():
    print("Knock knock")
    response1 = input('type here: ')
    response1_choices = ['who', 'whos there', 'whose there', 'who', 'who is there','whos there?', "who's there", "who's there"]
    response2_choices = ['europe who?', 'europe who']
    if response1 in response1_choices:
        print("Europe")
        response2 = input('type here: ')
        response2 = response2.lower()
        if response2 in response2_choices:
            print("I'm not a poo, you're a poo!")
        else:
            print("check your spelling!")
    else:
        print("check your spelling!")
def menu():
    sides = ["potato salad","mashed potatoes", "bowl of soup", "garden salad", "salsa", "green beans", "fruit salad"]
    mainCourses = ["steak,", "fried chicken", "chicken tacos", "hamburger", "pulled pork", "roast beef sandwich", "mostacolli"]
    beverages = ["soda", "water", "iced tea", "beer", "wine", "lemonade", "fruit juice"]
    desserts = ["chocolate chip cookies", "chocolate covered strawberries", "vanilla cake", "cheesecake", "ice cream", "brownie"]

    randomSide = random.choice(sides)
    randomMainCourse = random.choice(mainCourses)
    randomBeverage = random.choice(beverages)
    randomDessert = random.choice(desserts)

    print("You ordered " + randomMainCourse + " with a side of " + randomSide + " and " + randomDessert + " for dessert. You ordered " + randomBeverage + " to drink.")
def hangman():
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


def process_input(answer):
    if answer == "hi":
        greeting()
    elif answer == "exit":
        exit()
    elif answer == "tell a joke":
        tell_a_joke()
    elif answer == "what's the weather":
        weather()
    elif answer == "rock paper scissors":
        rock_paper_scissors()
    elif answer == "haiku":
        haiku()
    elif answer == "knock knock":
        knock_knock()
    elif answer == 'menu':
        menu()
    elif answer == 'hangman':
        hangman()
    else:
        say_default()


#answer = input("(What will you say?) ")
def say_greeting():
  print("Hey there!")

def say_default():
  print("That's cool!")
# --- Put your main program below! ---
def main():
  intro()
  while True:
    print("Say 'hi', 'tell a joke', 'what\'s the weather', 'rock paper scissors', 'haiku','knock knock', 'hangman', or 'menu'.")
    answer = input("Say something to me: ")
    process_input(answer.lower())
    return answer
    print()



# start calling code


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
