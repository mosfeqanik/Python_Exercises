import turtle

turtle.color("black")
turtle.speed(5)
turtle.shape("turtle")

def draw_shape():
		for i in range(4):
			turtle.forward(5)
			turtle.left(90)
		turtle.forward(5)

counter=0
while counter <90:
	draw_shape()
	turtle.right(4)
	counter +=1
turtle,exitonclick()