#Area Calculator

#This project is presented as a classwork so I will give you
#the problem statement first.

#When the program starts, it should display a message saying:
 #   "Welcome to the Area Calculator designed by ...[Your Name]". It should display a menu of:

#Triangle
#Square
#Circle
#The algorithm for this program is given below:

'''
Display the welcome message: "Welcome to the Area Calculator designed by [Firstname Lastname]"
Display the shape menu showing the shapes you want them to find the area of
Ask the user to choose a shape [shapeNumber]
Use the shapeNumber to determine the procedure for the shape chosen by the user
If the shapeNumber is not in the menu, display an error message
The code for this project will be built up gradually and explained. First off, create a script called area.py.

Step 1

To display the welcome message, we enter the code shown below:

#Diplay the welcome message
print("Welcome to the area calculator created by Ajibola Oladubu")

Step 2

To display the shape menu, we have to use the ASCII Linefeed character which is \n. The code to do this is shown below:

#Display the shape menu
print("1 Triangle\n2 Square\n3 Circle")

Step 3

The variable we will need to declare at this point is the shapeNumber. Here we will need that variable to be an integer so we will use the int() function to perform a cast. The code for this is shown below:

#Ask the user to choose a shape
shapeNumber = int(input("Please choose a shape from the menu above"))

Step 4

In this part, we use the shapeNumber to know which shape the user wants its area calculated. The first stage of the code is shown below:

#Use the shape number to determine the shape to have its area calculated
if(shapeNumber ==1):
	print("Area of a Triangle")
elif(shapeNumber ==2):
	print("Area of a Square")
elif(shapeNumber ==3):
	print("Area of a Circle")
else:
	print("invalid selector")

'''

#This is a good place to test your code. Run the program and test that everything is working.

#Now that you have confirmed that your code works exactly, you can take the code from the script files for the respective shape and place them here. The code for our triangle now becomes:

#For Triangle

'''
print("Area of a triangle")
breadth = int(input("Enter the breadth of the traingle: "))
height = int(input("Enter the height of the triangle: "))
area = breadth * height/2
print("The area of the traingle is", area)
'''

#The code for the area of a square is:

'''
print("Area of a Square")
length = int(input("Enter the length of the square: "))
length = int(length)
area = length * length
print("The area of the square is: ", area)
'''


#For the Circle , we do:
#Before you run this program, you must import the math module. The code to to this is: import math.

#Place the import math statement at the top of your script and run your program.


'''
print("Area of a Circle")
radius = int(input("Enter the radius"))
area = radius * radius * math.pi
area = round(area, 2)
print("The area of the circle is", area)
'''
