def find_fib(n):
	fib_x=1
	fib_next=1
	if n<=2:
		fib_n=1
		return fib_n
	else:
		i=3
		while i<=n:
			i+=1
			fib_temp=fib_x+fib_next
			fib_x=fib_next
			fib_next=fib_temp
		fib_n=fib_next
		return fib_n
def list_fib(n):
	fib_list=[1,1]
	fib_x=1
	fib_next=1
	if n<=2:
		fib_n=1
		return fib_list[:n]
	else:
		i=3
		while i<=n:
			i+=1
			fib_temp=fib_x+fib_next
			fib_x=fib_next
			fib_next=fib_temp
			fib_list.append(fib_next)
		fib_n=fib_next	
	return fib_list
for x in range(1,11):
	print(find_fib(x))
for y in range(1,11,1):
	print(list_fib(y))


