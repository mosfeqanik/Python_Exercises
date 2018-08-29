import random
number= random.randint(1,1000)
attempts=0
low=1
high=1000

while True:
	print("Guess the number (between 1 to 1000):")
	input_number=(low+high)//2 #only integer division
	print("my guess is",input_number)
	attempts += 1
	if input_number== number:
		print("yes,your guess is correct")
		print(input_number)
		print(number)
		break
	elif input_number>number:
		print("Incorrect,please try to guess a smaller number")
		high=input_number-1
		print(input_number)
		print(number)

	else:
		print("Incorrect,please try to guess a greater number")
		low=input_number+1
		print(input_number)
		print(number)
		

print("you tired",attempts,"times to find the correct number.")
