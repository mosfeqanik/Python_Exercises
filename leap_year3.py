year= raw_input("put your year")
year=int(year)

if year %100!=0 and year %4==0:
	print("yes")
elif year %100==0 and year %400==0:
	print("yes")
else:
	print("No")



