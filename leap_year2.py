year= raw_input("put your year")
year=int(year)
if year %400==0:
	print("yes")
elif year %100==0:
	print("No")
elif year %4==0:
	print("Yes")
else :
	print("No")

