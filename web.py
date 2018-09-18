import requests
url="https://goo.gl/images/CNKdys"
r=requests.get(url)
with open("images.png","wb")as f:
	f.write(r.content)
