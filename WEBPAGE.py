import requests
import os
import webbrowser as web

url="http://dimik.pub/"
response=requests.get(url)
with open("dimik.html","w") as f:
	f.write(response.text)

file_path=os.path.realpath("dimik.html")
print(file_path)
web.open("file://"+file_path)