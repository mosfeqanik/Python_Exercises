lines=["this is first line","this is second line","this is three line"]
with open("files.txt","w")as f:
	for line in lines:
		f.write(line+"\n")