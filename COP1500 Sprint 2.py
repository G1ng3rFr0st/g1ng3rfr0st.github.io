#Jack Garrison
#For my integration project I have decided to create a text based game inspired by my infatuation with the cosmic horror genre of story telling.
#The working title for the game right now is "Discarded"
flag = True
def _menu_():
    while flag == True:
        print("Welcome to 'Discarded'\nPlease enter the number of each selection to fill it out accordingly. This will be important for the game. Enter 3 when you are done and enter 4 if you want to quit.")
        print("1. Character Creation\n2.Begin the game!\n3. Quit")
        selection = input()
        if selection == "1":
            print("Enter your name: ")
            name = input()
            print("Enter the year you were born: ")
            year = input()
            print("Enter your favorite color: ")
            favColor = input()
        elif selection == "2":
            print("Let's Begin", name + "!")
            _game_(name, year, favColor)
            flag == False
        elif selection == "3":
            quit()
        else:
            print("Please enter a valid selection.")
            _menu_()
#This menu will be helpful to give the program a more game like feel.
def gameQuestions():
    total = 0
    for y in range(3):
        playerAnswers = int(input("Please enter a number between 1 and 5: "))
        total += playerAnswers
        if y == 0:
            answer1 = total
        elif y == 1:
            answer2 = total
        elif y == 2:
            answer3 = total
    answer1 = answer1 / 20
    answer2 = answer2 * 4 * 2
    answer3 = answer3 % 3
    # Above, I am using the /, *, and % math operators to answer the questions quickly for the player so they don't need a calculator.
    print("You were always a star when it came to mental math, and now it feels like there was a reason for that. You begin turning the padlock to the answers for the problems: ")
    print(format(answer1,'.2f'), " left, ", answer2, " right, ", answer3, " left again.", sep="")
def _game_(name, year, favColor, ):
    print("You wake up in a dark, damp room with a strange object in your hand...\nUnsure of where or how you obtained it, you can't even recall how you arrived at this unknown location in the first place.")
    print("You swear you can hear a voice calling out to you faintly like a whisper, but there is no one else with you.\nThe voice is repeating: ", end="")
    #Here, I am using the * operator to repeat the string 'home' over and over to give off the unsettling feeling of a single word repeating over and over again as if it was a whisper.
    print("'" + "home" * 10 + "'")
    presentYear = int(year) + 22
    #Using the + operator here, I can take whatever the inputted number is, convert it into an integer, and have the code add 22 to it, allowing the user to put in any year they wanted for freedom of expression.
    print("You do your best to ignore the repeating voice, but it feels like it's getting louder. You think to yourself:\n'Come on....think of something to orient yourself'")
    date = input("What day was it again? (Month/Day): ")
    gameDate = date + " " + str(presentYear)
    #In this instance of the + operator, I am using it to concatenate the variables together into a coherent sentence, again allowing for freedom through input.
    print("It was " + gameDate + ", you thought to yourself.\nYour name is " + name + ", and you were looking through an old antique store when you saw something in the corner of your eye.")
    print("It's an old cylinder shaped item with weird spiral patterns etched into the dark wood that it's made out of. You're not sure why, but when you hold it,  you feel a strange sense of purpose.\nAlmost like you were MEANT to find it.")
    cashOnHand = float(input("Enter a dollar amount in 10s that you have on you in the form of 0.00: "))
    print("The object is only $2.45! Heck you could buy ", int(cashOnHand // 2.45), " of these things if they had them.\nA feeling overcomes you to buy it now. You can hardly contain your excitement!")
    #I used the // operator because I want the amount that you can buy to be displayed as a whole number that is accurate to how many of them you could actually buy.
    print("You begin to walk up to the counter to checkout, when suddenly a sharp ringing in your head stops you in your tracks...\nYou reel in pain as the noise makes your heart race and your head pound. There's flash of deep blue as if you were in a never ending oceanic expanse and the phrase 'home' sneaks it's way into your head loudly.")
    print("Just as quickly as they came, the strange sensations leave without a trace. You've never experienced anything like that before. You think to yourself:\n'I seriously gotta cut the energy drinks.'")
    newCashOnHand = cashOnHand - 2.45
    print("Since you still have $ ", newCashOnHand, ", you can still go get the toy you wanted to buy for your dog at home.")
    #Here I use the - operator so that I can explain how much money you'd have left when I make the game more complicated in the future.
    dead = False
    while not dead:
        pain = input("Enter a number between 1 and 10: ")
        painScale = int(pain) ** 3
        # I use the ** operator here so that the next text can show an exaggerated number for their pain in the story
        if painScale < 10 and painScale >= 1:
            print("Despite the strange sensation you got in your head, you shrug off the experience as if nothing happened.")
            dead = True
        elif painScale > 10 and painScale <800:
            print("The sensation you experienced just now continues to throb in your brain. It's almost unbearable, but begins to subside with time.")
            dead = True
        elif painScale >= 1000 or painScale < 1:
            print("The pain you feel was too unbearable, and you begin to feel your consciousness fade. You have died to the beings influence.")
            _menu_()
    print("The flashback ends and you're back in the mysterious room with the strange object. You're a little less confused than before but your head is still pounding.")
    print("You begin to stand up when all of a sudden you here the voice in your head whisper to you again: " + "'" + "come" * 10 + "'")
    print("Looking around the room in the direction you heard the voice come from, you see an old dilapidated dresser with strange symbols all over it. To the left, there's a desk with a pile of old books on it. To the right, there is a shelf with various bottles on it. Where do you want to go?")
    a = None
    while a != 1:
        direction = input("Where do you want to go? Input Left, Right, or Dresser: ")
        if direction == "Left":
            print("You walk up to the desk in the left corner of the room. There are piles of books and various papers with strange drawings and unrecognizable languages. You can't make any sense of it, yet it feels oddly familiar.")
        elif direction == "Right":
            print("You walk up to the old shelf that sits around eye level with you. The jars are caked in dust, but you can see small objects suspended in a cucumber green liquid. They look like organs or strange unknowable creatures, and the sight of it makes you shudder.")
        elif direction == "Dresser":
            print("You walk up to the dresser, the source of the voice you heard earlier. It's nearly rotted entirely, but something tells you it could never truly collapse. 'It' wouldn't want that.You spot a padlock keeping the doors from opening.")
            a = 1
    print("Near the padlock, there is a list of 3 problems etched into the wood that correlate to what you assume to be the 3 digits needed to unlock it, allowing whatever is inside to finally be free. They are as follows: ")
    print("'How often would 'I' wake if 'I' were to only sleep 20 years at a time'?\n'Four times 'I' was given new sets of eyes to see more clearly, how many do 'I' have now?'\nand\n'How many sets of eyes would remain if 'I' were to split them across 3 beings?'\nThe numbers begin flowing into your mind from somewhere unknown.")
    gameQuestions()
    print("The padlock snaps open, freeing the doors to be manipulated freely. But, they can't just be opened by anyone. They need to be opened by YOU. The voice won't stop saying this after all.")
    print("'" + "You" * 10 + "'")
    print("You open the doors slowly. Looking inside, there's the abyss you had seen before in the store you bought this item from. It's dark, expansive, and triggers a primal fear in you that you haven't experienced before.\nMost of all however, you are left asking yourself: 'What is this?'")
    colorOfEntity = favColor
    print("As you peer into this endless void, a large " + colorOfEntity + " arm approaches from the abyss with a plethora of other arms extending off of the main one. You struggle to comprehend it.\nBut, you have no time for that as it slowly and gently wraps its strange fingers around the artifact you're still holding. You haven't let it go since you woke up.")
    print("You slowly release the item to the 'Thing' as a wave of anxiety passes over you. You've come to realize something...")
    print("You, were just a tool. Nothing more than a means to get an object returned back to it's rightful owner. The object you were holding knew what it's purpose was, and was originally discarded accidentally by the 'Thing' now reclaiming it from you.\nThe object needed a means to return from your world, and you were that means " + name + ". Nothing more.")
    print("You, much like that object before have now been...\nDiscarded.\nThe End")
    print("Thank you for playing! I appreciate your time today!")
_menu_()