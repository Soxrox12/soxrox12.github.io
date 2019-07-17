#import JSON library to extend code
import json
#create the function to get survey answers
def survey():
    '''data_list = []'''
    #create a variable to run the 1st while loop (survey q's)
    again = True
    #create empty dictionary to store user's survey answers
    user_input = {}
    #while loop containing survey questions
    #create empty lists to hold dictionary values
    name = []
    birthday = []
    age = []
    home = []
    siblings = []
    color = []
    app = []
    show = []
    while again == True:
        name.append(input("What is your name?  "))
        birthday.append(input("What is your birthday?  "))
        age.append(input("How old are you?  "))
        home.append(input("Where do you live?  "))
        siblings.append(input("How many siblings do you have?  "))
        color.append(input("What is your favorite color?  "))
        app.append(input("What is your favorite social media app?  "))
        show.append(input("What is your favorite TV show or movie?  "))
        #add user's survey answers to user_input dictionary
        user_input = {
            'Name': name,
            'Birthday': birthday,
            'Age': age,
            'Home': home,
            'Siblings': siblings,
            'Color': color,
            'App': app,
            'TV': show
        }
        '''data_list.append(user_input)'''
        #answers.append(user_input)
        #create variable to run 2nd while loop (answer questions again or not)
        '''playing = True
        #begin while loop
        while playing == True:
            #ask if user wants to answer survey again (allows multiple ppl)
            play_again = input("Do you want to answer these questions again? (Type 'yes' or 'no')  ")
            play_again.lower()
            #if user answers 'yes', set 2nd while loop to false to exit, and go back to survey loop
            if play_again == "yes":
                again = True
                playing = False
            #if user answers 'no', set first while loop condition to false to terminate both loops and move to categories function
            elif play_again == "no":
                again = False
                playing = False
            #gives programmer way to exit program in case of forever loop
            elif play_again == "exit":
                exit()
            #catch-all in case user inputs something wrong. Goes through 2nd loop again
            else:
                print("You typed something incorrectly, try again.")
                continue
        '''
        #return user_input so categories function can access it
        return user_input
        '''return data_list'''

#categories function allows user to display just one key's values
def categories(user_input):
    #set variable to determine while loop
    category = True
    #while loop to display categories
    while category == True:
        display = input("Would you like to see a certain category? (Type, 'names', 'ages', 'birthdays', 'homes', 'siblings', 'colors', 'apps', 'TV', or 'all'.)  ")
        #if user answers 'names', display only the values under the name key
        if display == "names":
            print(user_input['Name'])
            category = False
        elif display == "ages":
            print(user_input['Age'])
            category = False
        elif display == "birthdays":
            print(user_input['Birthday'])
            category = False
        elif display == "homes":
            print(user_input['Home'])
            category = False
        elif display == "siblings":
            print(user_input['Siblings'])
            category = False
        elif display == "colors":
            print(user_input['Color'])
            category = False
        elif display == "apps":
            print(user_input['App'])
            category = False
        elif display == "TV":
            print(user_input['TV'])
            category = False
        elif display == "all":
            print(user_input)
            category = False
        elif display == 'exit':
            exit()
        else:
            print("I didn't understand that, try again please!")
            continue

def main():
    #run the survey function, get answers and store them in user_input
    data_list = []
    getMoreData = True
    while getMoreData == True:
        user_input = survey()
        data_list.append(user_input)
        #run the categories function using data in user_input
        categories(user_input)
        asking = input("Do you want to add more data (take the survey again)?  ")
        if asking == 'yes':
            continue
        else:
            getMoreData = False
        '''else:
            print("You have typed something incorrectly, type 'yes' or 'no' please.  ")
        '''
    #set variable to run while loop
    more_categories = True
    #loop to ask user if they want to see another category or restart survey
    while more_categories == True:
        moreC = input("Do you want to see another category? Type 'yes' to see categories or type 'no' to restart. Type JSON to see the JSON file with the user_input dictionary.  ")
        #if user answers yes, restart categories function to display another category; terminate current loop
        if moreC == 'yes':
            categories(user_input)
            more_categories = False
        #if user answers no, return to survey function to allow another user to answer; terminate current loop
        elif moreC == 'no':
            survey()
            more_categories = False
        elif moreC == 'JSON':
            more_categories = False
            continue
        elif moreC == exit:
            exit()
        else:
            print("Remember to only type 'yes' or 'no'")
            continue

    print("it worked")
    output_file = open("survey.json", 'w', encoding = 'utf-8')
    for dic in data_list:
        json.dump(dic, output_file)
        output_file.write("\n")
'''    with open('survey.txt', 'w') as outfile:
        json.dump(user_input, outfile)
    survey_json = json.dumps(user_input)
    print(survey_json)
    #print(answers)
'''
if __name__ == '__main__':
    main()
