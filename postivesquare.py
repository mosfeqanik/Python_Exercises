while True:
	n=raw_input("please enter a number (0 to exit): ")
	n=int(n)
	if n<0:
		print("We only allow positive number.please try again")
		continue
	if n==0:
		break
	print("square of",n,"is",n*n)