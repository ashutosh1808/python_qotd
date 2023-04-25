import requests

urladd="https://www.forbes.com/forbesapi/thought/uri.json?enrich=true&query=1&relatedlimit=5"
res=requests.get(urladd)


data=res.json()
#print(data)
qotd=data['thought']['quote'].strip()
print(qotd)