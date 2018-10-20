import requests
url="http://dimikcomputing.com"
response =requests.get(url)
with open("write.html","w",encoding=response.encoding)as f:
		f.write(response.text)