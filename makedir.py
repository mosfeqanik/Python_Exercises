import os
# dir_name="dimik_pub"
# os.mkdir(dir_name)

def create_directory(newname):
	try:
		os.mkdir(newname)
	except FileExistsError:
		print(newname,"already exists")

create_directory(dimik_pub)