while True:
	try:
		x=int(input("please put a number"))
		break
	except:
		print("it is not correct please put a number")
	finally:
		print("over")