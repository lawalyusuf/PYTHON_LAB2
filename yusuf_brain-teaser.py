
print("Welcome to LOYA Brain Teaser")
print("Enter the number for your option")
play_again = ""
score = 0

while(play_again.lower() != "x"):

    
    question1 = input("A student who can combine chemicals is a?\n1 Commercial Student\n2 Science Student\n3 Art Student\n4 Technical Student\n  ")
    if (question1 == "2"):
        print("You are correct")
        score = score + 1
    else:
        print("You are wrong")

    question2 = input("Which African country was never colonized?\n1 Wakanda\n2 Benin\3 Ethiopia\n4 Nigeria\n  ")
    if (question2 == "3"):
        print("You are correct")
        score = score + 1
    else:
        print("You are wrong")

    question3 = input("LCD or LED monitors are also called?\n1 vertical panal display\n2 round panael display\n3 flat panel display\n4 straight panel displays\n  ")
    if (question3 == "3"):
        print("You are correct")
        score = score + 1
    else:
        print("You are wrong")


    question4 = input("One of the following cannot be connected to the computer?\n1 microphone\n2 light pen\n3 mouse\n4 none of the above\n ")
    if (question4 == "4"):
        print("You are correct")
        score = score + 1
    else:
        print("You are wrong")
                      
    question5 = input("Power button, DVD drive, audio port are found in the ----- of the computer case?\n1 side\n2 back\n3 front\n4 under\n ")
    if (question5 == "3"):
        print("You are correct")
        score = score + 1
    else:
        print("You are wrong")

    print("Your score is:", score)
    score = 0
    
    play_again = input("Do you want to play again? Press X to exit or Enter to continue:\n ")
    
