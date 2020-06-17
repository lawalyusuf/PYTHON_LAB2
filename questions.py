'''
Question:

a) ## This programs asks a user for a name and a password.
# It then checks them to make sure the user is allowed in.

1. Ask the user for a number. Depending on whether the number
is even or odd, print out an appropriate message to the user.

1b. Python Program to Check Prime Number

2.  Let’s say I want to make a piece of code that converts from a numerical
grade (1-100) to a letter grade (A, B, C, D, F)

3. In this program, you'll learn to find the largest among three numbers using
if else and display it.

4. Python program to check if a number is positive, negative or zero

'''




#Solution
#a
'''
# It then checks them to make sure the user is allowed in.

name = raw_input("What is your name? ")
password = raw_input("What is the password? ")
if name == "Josh" and password == "Friday":
    print "Welcome Josh"
elif name == "Fred" and password == "Rock":
    print "Welcome Fred"
else:
    print "I don't know you."
'''

#1.
'''
num = input("Enter a number: ")
mod = num % 2
if mod > 0:
    print("You picked an odd number.")
else:
    print("You picked an even number.")
'''

#1b
'''
# Python program to check if the input number is prime or not

num = 407

# take input from the user
# num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")
'''

#2
'''
grade = input("Enter your grade: ")
if grade >= 90:
 print("A")
elif grade >= 80:
 print("B")
elif grade >= 70:
 print("C")
elif grade >= 65:
 print("D")
else:
 print("F")
'''

#3
'''
# Python program to find the largest number among the three input numbers

# change the values of num1, num2 and num3
# for a different result
num1 = 10
num2 = 14
num3 = 12

# uncomment following lines to take three numbers from user
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number between",num1,",",num2,"and",num3,"is",largest)
'''

#4
'''

num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

           or

num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")
'''
