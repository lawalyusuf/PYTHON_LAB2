import random

n = random.randint(1, 99)


#The randint() function is provided by the random module, so you must precede it with random. (don’t forget the period!) to tell Python that the function randint() is in the random module.

#The randint() function will return a random integer between (and including) the two integer arguments you pass to it. Line 9 passes 1 and 20 between the parentheses separated by commas that follow the function name. The random integer that randint() returns is stored in a variable named number; this is the secret number the player is trying to guess.

#Just for a moment, go back to the interactive shell and enter import random to import the random module. Then enter random.randint(1, 20) to see what the function call evaluates to. It will return an integer between 1 and 20. Repeat the code again and the function call will return a different integer. The randint() function returns random integer each time, just as rolling dice you’ll get a random number each time:


guess = int(raw_input("Enter an integer from 1 to 99: "))
while n != "guess":
    print
    if guess < n:
        print "guess is low"
        guess = int(raw_input("Enter an integer from 1 to 99: "))
    elif guess > n:
        print "guess is high"
        guess = int(raw_input("Enter an integer from 1 to 99: "))
    else:
        print "you guessed it!"
        break
    print
