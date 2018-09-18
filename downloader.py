import requests
import sys
base_url="http://subeen.com/download/"
info_dt={"name":"subeen","email":"book@subeen.com","country":"Bangladesh"}
print(type(info_dt))
url=base_url+"process.php"

response=requests.post(url, data=info_dt)
if response.ok is False:
	sys.exit("error downloading the file")

with open("cpbook.pdf","wb") as f:
	f.write(response.content)

print("Book download complete!")