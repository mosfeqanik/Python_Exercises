import turtle

height=5
width=8
turtle.speed(2)
# turtle.penup()
for y in xrange(height):
	for x in xrange(width):
		turtle.dot()
		turtle.forward(20)
	turtle.backward(20*width)
	turtle.right(90)
	turtle.forward(20)
	turtle.left(90)
turtle.exitonclick()



