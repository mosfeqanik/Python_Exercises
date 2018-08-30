def isprime(n):
	if n==2:
		return True
	if n%2<0:
		return False
	if n%2==0:
		print(n,"is divided by 2")
		return False
	prime=True
	m=n//2+1
	for x in range(3,m,2):
		if n%x==0:
			print(n,"is divided by",x)
			prime=False
			return prime
	return prime
while True:
	input_number=input("put your number")
	input_number=int(input_number)
	if input_number==0:
		break
	prime=isprime(input_number)
	if prime is True:
		print(input_number,"is a prime number")
	else:
		print(input_number,"is not a prime number")	