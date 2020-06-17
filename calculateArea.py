import math
print("Welcome to the area calculator created by 'Jibola J'Oladubu")
print("1 Triangle\n2 Square\n3 Circle")
shapeNumber = int(input("Please choose a shape from the menu above: "))
if(shapeNumber ==1):
	print("Area of a Triangle")
	breadth = int(input("Enter the breadth of the traingle: "))
	height = int(input("Enter the height of the triangle: "))
	area = breadth * height/2
	print("The area of the traingle is", area)
elif(shapeNumber ==2):
	print("Area of a Square")
	length = int(input("Enter the length of the square: "))
	area = length * length
	print("The area of the square is: ", area)
elif(shapeNumber ==3):
	print("Area of a Circle")
	radius = int(input("Enter the radius"))
	area = radius * radius * math.pi
	area = round(area, 2)
	print("The area of the circle is", area)
else:
	print("You entered an Invalid Selector")
	print("Run the program again and select an option from 1 to 3")

