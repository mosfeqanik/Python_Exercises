import turtle
name=raw_input('what is your name?')
name=name.lower()
if name.startswith("mr"):
	print("hello sir,how are you")
elif name.startswith("mrs") or name.startswith("miss") or name.startswith("ms"):
	print("hello madam,how are you")
else:
	name=name.capitalize()
	str="Hi"+name+"! How are you?"
	print (str)
turtle.exitonclick()