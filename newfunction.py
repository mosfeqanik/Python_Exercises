nums = [9, 8, 7, 6, 5]
nums.append(4)
nums.insert(2, 11)
print(len(nums))
numbers = list(range(10))
print(numbers)
nums = list(range(5))
print(nums)
print(nums[4])
nums = list(range(5, 8))
print(nums)
print(len(nums))

list = [1, 1, 2, 3, 5, 8, 13]
print(list)
print(list[4])
print(list[list[4]])

list = [1, 2, 3]
for var in list:
	print(var)
def myfnc(x):
	print("inside myfnc",x)
	x=10
	print("inside myfnc",x)

x=20
myfnc(x)
print(x)

