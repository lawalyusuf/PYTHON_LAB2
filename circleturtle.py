import turtle

'''
Filled Circle

To draw a filled circle, we have to use the circle function.
To fill the circle, we use the begin_fill() function before
we write the code to draw the circle and the end_fill() after
we write the code to draw the circle. The code to do this is shown below:
'''

turtle.pensize(10)
turtle.color("black", "gold")
turtle.begin_fill()
turtle.circle(60)
turtle.end_fill()
