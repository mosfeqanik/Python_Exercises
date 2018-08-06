import turtle

turtle.color("black")
turtle.speed(5)
turtle.shape("turtle")



counter =0
for counter in range(1,36,1):
	for i in range (4):
		turtle.forward(100)
		turtle.right(90)
	turtle.right(10)

	

turtle.exitonclick()
