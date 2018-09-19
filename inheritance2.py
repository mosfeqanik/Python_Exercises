class Vehicles:
	"""Based class"""
	def __init__(self,name,manufacturer,color):
		print("Creating a vehicles") 
		self.name=name
		self.manufacturer=manufacturer
		self.color=color

	# def drive(self):
	# 	print("driving",self.manufacturer,self.name)


	# def turn(self,direction):
	# 	print(self.name,"turning to",direction)

	# def brake(self):
	# 	print(self.name,"is stoping")	



class car(Vehicles):
	"""class for car"""


	def __init__(self,name,manufacturer,color,year,wheels):
		print("Creating a car")
		super().__init__(name,manufacturer,color)
		# self.name=name
		# self.manufacturer=manufacturer
		# self.color=color
		self.year=2017
		self.wheels=4
		# print("a new car has been created .name:",self.name)
		# print("it has ",self.wheels,"wheels")
		# print("the car was built in ",self.year)
	# def change_gear(self,gear):
	# 	print(self.name,"is changing gear to",gear)

	# def turn(self,direction):
	# 	print("turning",self.name,"to",direction)

if __name__=="__main__":
	c=car("mustang","ford","red","2018",4)
	# v1=Vehicles("softail delux","harley-Davidson","blue")
	# c.turn("left")
	# v1.drive()
	# v1.turn("right")
	# v1.brake()
	# c.change_gear("p")
	print(c.name,c.year,c.wheels)

