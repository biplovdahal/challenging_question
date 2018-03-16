import requests

data={
	'first_name':'biplovdahal',
	'last_name':'testing',
	'phone_number':'5107344513',
	'email':'dahalbiplovechs@gmail.com',
	'role':'regular',


}

## try:
# 	if data['id']:

# 	print(data['id'])
# except:
# 	print 'error happened'
r = requests.post('http://127.0.0.1:8000/api/members',data=data)
print(r.text)

curl -X POST -H "Content-Type:application/json"  -d '{"first_name":"test1","last_name":"test2","phone_number":"510734"}' 'http://127.0.0.1:8000/api/members'