Hey! I've written instructions as instructed in the email you sent me!

I've used swagger to list my urls out

/api/docs (To see the list of URLS)


INSTRUCTIONS:</br></br>
1. Clone this project</br></br>
2. You could setup virtualenv too or skip this process (Mac): virtualenv -p python3 env && source env/bin/activate</br></br>
3. Install the dependencies: pip3 install -r dependencies.txt</br></br>
4. Run the development server: python3 manage.py runserver</br></br>
5. Go to /api/docs to see brief info.



<h1> API ENDPOINTS </h1>

<b>GET /members (Gives all the members in our mysql db)</b>

curl 'http://127.0.0.1:8000/api/members/' 



<b>POST /members (Creates a new member)</b>

curl 'http://127.0.0.1:8000/api/members/' -H 'Pragma: no-cache' -H 'Origin: http://127.0.0.1:8000' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.9' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36' -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'Cache-Control: no-cache' -H  -H 'Referer: http://127.0.0.1:8000/api/docs/' -H  -H 'Connection: keep-alive' -H 'DNT: 1' --data-binary $'{\n  "first_name": "foo",\n  "last_name": "bar",\n  "phone_number": "5140734",\n  "email": "foobar@gmail.com",\n  "role": "1"\n}' --compressed







<b>PUT /members (Updates a member)</b>

curl -X PUT -H "Content-Type:application/json"  -d '{"id":"1", first_name":"Biplov","last_name":"Dahal","phone_number":"510734","email":"dahalbiplovechs@gmail.com","role":"regular"}' 'http://127.0.0.1:8000/api/members'


<b>DELETE /members (Deletes a member)</b>

curl 'http://127.0.0.1:8000/api/members/10/' -X DELETE -H 'Pragma: no-cache' -H 'Origin: http://127.0.0.1:8000' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.9' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36' -H 'Accept: application/json' -H 'Cache-Control: no-cache' -H 'Referer: http://127.0.0.1:8000/api/docs/' -H  -H 'Connection: keep-alive'  -H 'DNT: 1' --compressed
