def div(a,b):
	try:
		return a/b
	except ZeroDivisionError:
		print("can not divide by Zero")
	except TypeError:
		print("unsupported type.didyou use string?")
print(div(10,2))
print(div(3,2))
print(div("3",2))
print(div(2,0))

