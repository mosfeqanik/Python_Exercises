def is_prime3(n):
	if n==2:
		return True
	if n%2==0:
		print(n,"is divisible by 2")	
		return False
	if n%2<0:
		return False
	prime=True
	m=n//2+1
	for x in range(3,m,2):
		if n%x==0:
			print(n,"is divisible by",x)
			prime=False
			return prime
	return prime

while True:
	number=input("Guess the number (enter 0 to exit):")
	number=int(number)
	if number== 0:
		break
	prime=is_prime3(number)
	if prime is True:
		print(number,"is a prime number")
	else:
		print(number,"is not a prime number")