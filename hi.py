while True:
	try:
		x=int(input("put your number"))
		print(x)
		break
	except:
		print("please write correctly")
	finally:
		print("over")		

