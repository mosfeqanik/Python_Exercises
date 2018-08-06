terminate_program=False
while not terminate_program:
	number1=raw_input("please enter a number:")
	number1=int(number1)
	number2=raw_input("please enter another number:")
	number2=int(number2)

	while True:
		operation=raw_input("please enter add/sub or quit to exit:  ")

		if operation == "quit":
			terminate_program=True
			break
		if operation not in ["add","sub"]:
			print("Unknown operation!")
			break
		if operation == "add":
			print("Result is",number1+number2)
			break
		if operation == "sub":
			print("Result is",number1-number2)
			break