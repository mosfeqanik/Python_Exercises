import math

def is_prime5(n):
	if n==2:
		return True
	if n%2==0:
		return False
	if n<2:
		return False
	m=math.sqrt(n)
	m=int(m)+1
	for x in range(3,m,2):
		if n%x==0:
			return False
	return True

while True:
	number=input("Guess the number (enter 0 to exit):")
	number=int(number)
	if number== 0:
		break
	prime=is_prime5(number)
	if prime is True:
		print(number,"is a prime number")
	else:
		print(number,"is not a prime number")
