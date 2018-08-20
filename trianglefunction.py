import turtle

turtle.color("black")
turtle.speed(5)
turtle.shape("turtle")

def draw_triangle():
		arm=raw_input("please the value of parametre		")
		arm=int(arm)
		for i in range(3):
			turtle.forward(arm)
			turtle.left(120)
		turtle.forward(arm)
draw_triangle()
turtle.exitonclick()




