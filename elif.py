#It is possible to chain several if statements together using the else...if statement. Python abbreviates this as elif.

#Example if/elif/else statement

temperature = int(input("What is the temperature in Fahrenheit? "))
if temperature > 90:
    print("It is hot outside")
elif temperature < 30:
    print("It is cold outside")
else:
    print("It is not hot outside")
print("Done")




#Text Comparisons
'''
It is possible to use an if statement to check text.


user_name = input("What is your name? ")
if user_name == "Paul":
    print("You have a nice name.")
else:
    print("Your name is ok.")

'''
