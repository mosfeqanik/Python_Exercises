class car:
	def __init__ (self,n,c):
		self.name=n
		self.color=c
	def start(self):
		print("my car is ",self.name)
		print("my car color is ",self.color)
		print("the engine is started")

my_car1=car("audi","grey")
# my_car1.start()
my_car1.year=2017
print(my_car1.name,my_car1.color,my_car1.year)

# my_car2=car("corrilla","white")
# my_car2.start()
# my_car3=car("axio","red")
# my_car3.start()
# my_car4=car("allion","black")
# my_car4.start()


