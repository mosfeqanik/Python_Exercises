class car:

	def __init__(self,n,c):
		self.name=n
		self.color=c
		
	def startengine(self):
		print("engine is starting")

car=car("corollia","black")
car.startengine()
car.year=2017
print(car.name,car.color,car.year)
