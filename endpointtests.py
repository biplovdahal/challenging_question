import requests

data={
	'id':'1'

}

## try:
# 	if data['id']:

# 	print(data['id'])
# except:
# 	print 'error happened'
r = requests.delete('http://127.0.0.1:8000/api/members',data=data)
print(r.text)
# # print(r.text)