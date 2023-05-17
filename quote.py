import requests

try:
	url="http://api.quotable.io/random"
	res=requests.get(url)
	data=res.json()
	print(data['content'])
except Exception as e:
	print("Issue: ",e)
