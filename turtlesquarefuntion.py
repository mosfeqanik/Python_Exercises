import turtle

turtle.color("black")
turtle.speed(5)
turtle.shape("turtle")

def draw_shape(shape):
	if shape =="square":
		for i in range(4):
			turtle.forward(50)
			turtle.left(90)
		turtle.forward(75)
	if shape =="triangle":
		for i in range(3):
			turtle.forward(75)
			turtle.left(120)
		turtle.forward(75)
draw_shape("square")
draw_shape("triangle")
turtle.exitonclick()