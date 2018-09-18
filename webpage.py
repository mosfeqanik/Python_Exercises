import requests
url="http://dimik.pub/"
response=requests.get(url)
with open("dimik.html","w") as f:
	f.write(response.text)