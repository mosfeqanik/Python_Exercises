import random
number= random.randint(0,1000)
attempts=0


while True:
	input_number=input("Guess the number (enter 0 to exit):")
	input_number=int(input_number)
	attempts += 1
	if input_number== number:
		print("yes,your guess is correct")
	elif input_number>number:
		print("Incorrect,please try to guess a smaller number")
		print(input_number)
		print(number)

	else:
		print("Incorrect,please try to guess a greater number")
		print(input_number)
		print(number)


print("you tired",attempts,"times to find the correct number.")
