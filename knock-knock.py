def knock_knock():
    print("Knock knock")
    response1 = input('type here: ')
    if response1 == "who's there":
        print("Europe")
        response2 = input('type here: ')
        response2 = response2.lower()
        if response2 == 'europe who' or 'europe who?':
            print("I'm not a poo, you're a poo!")
        else:
            print("check your spelling!")
    else:
        print("check your spelling!")

knock_knock()
