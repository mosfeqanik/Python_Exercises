import requests
import os
import webbrowser as wb


url="https://dimikcomputing.com/"
res=requests.get(url)

with open("dimik.html","w")as f:
	f.write(res.text)

file_path=os.path.realpath("dimik.html")
print(file_path)
wb.open("file://"+file_path)