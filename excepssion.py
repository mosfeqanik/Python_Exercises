# import io

filename="files.txt"
mode="r"

try:
	with open(filename,mode)as f:
		content=f.read()
		print(content)
except FileNotFoundError:
	print(filename,"not found.please check if the file's name is correct")
# except io.UnsupportedOperation:
# 	print ("Are you sure",filename,"is readable")