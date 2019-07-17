#imports the ability to get a random number (we will learn more about this later!)
from random import *
print("")
print("Let's start with LEVEL 1")
print("")
#Create the list of words you want to choose from.
firstNames = ["Hannah","Taylor","Madison","Elmo","Mickey","Bryan","Mario", "Eli", "Becky", "Larry"]
lastNames = ["Travis", "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson"]

#Generates a random integer.
randomIndex = randint(0, len(firstNames)-1)
randomLastName = randint(0, len(lastNames)-1)
print("I think your name is " + firstNames[randomIndex] + " " + lastNames[randomLastName])

print("")
print("")
print("Now for LEVEL 2!")
print("")

sides = ["potato salad","mashed potatoes", "bowl of soup", "garden salad", "salsa", "green beans", "fruit salad"]
mainCourses = ["steak,", "fried chicken", "chicken tacos", "hamburger", "pulled pork", "roast beef sandwich", "mostacolli"]
beverages = ["soda", "water", "iced tea", "beer", "wine", "lemonade", "fruit juice"]
desserts = ["chocolate chip cookies", "chocolate covered strawberries", "vanilla cake", "cheesecake", "ice cream", "brownie"]

randomSide = randint(0, len(sides)-1)
randomMainCourse = randint(0, len(mainCourses)-1)
randomBeverage = randint(0, len(beverages)-1)
randomDessert = randint(0, len(desserts)-1)

print("You ordered " + mainCourses[randomMainCourse] + " with a side of " + sides[randomSide] + " and " + desserts[randomDessert] + " for dessert. You ordered " + beverages[randomBeverage] + " to drink.")

print("")
print("")
print("Now for the final level, LEVEL 3")
print("")
fiveSyllables = ["Imagination","Nationalism","Anticipation", "Emotionally,"]
fiveSyllables2 = ["Oh, give me a break", "The truth is out there", "We are not alone", "Old habits die hard", "Practice makes perfect"]
sevenSyllables = ["All the very best to you", "Curiosity is good", "Learn the art of listening","I like to cook spaghetti","Oxygen is poisonous", "It was the best of times, NOT", "The story ends with a kiss"]

randomFiveSyllables1 = randint(0, len(fiveSyllables)-1)
randomFiveSyllables2 = randint(0, len(fiveSyllables2)-1)
randomSevenSyllables = randint(0, len(sevenSyllables)-1)

print("Here is your haiku:")
print(fiveSyllables[randomFiveSyllables1])
print(sevenSyllables[randomSevenSyllables])
print(fiveSyllables2[randomFiveSyllables2])
print("")
print("")
