Hey! I've written instructions as instructed in the email you sent me!

I've used swagger to list my urls out

/api/docs (To see the list of URLS)


INSTRUCTIONS:</br></br>
1. Clone this project</br></br>
2. You could setup virtualenv too or skip this process (Mac): virtualenv -p python3 env && source env/bin/activate</br></br>
3. Install the dependencies: pip3 install -r dependencies.txt</br></br>
4. Run the development server: python3 manager.py runserver</br></br>
5. Go to /api/docs to see brief info.



<h1> API ENDPOINTS </h1>

GET /members (Gives all the members in our mysql db)
curl -X GET "Content-Type:application/json" http://127.0.0.1:8000/api/members


POST /members

curl -X POST -H "Content-Type:application/json"  -d '{"first_name":"Biplov","last_name":"Dahal","phone_number":"510734","email":"dahalbiplovechs@gmail.com","role":"regular"}' 'http://127.0.0.1:8000/api/members'



PUT /members [id field IS MANDATORY]

curl -X PUT -H "Content-Type:application/json"  -d '{"id":"1", first_name":"Biplov","last_name":"Dahal","phone_number":"510734","email":"dahalbiplovechs@gmail.com","role":"regular"}' 'http://127.0.0.1:8000/api/members'


DELETE /members [id FIELD IS MANDATORY]

curl -X DELETE "Content-Type:application/json"  -d '{"id":"1"}' 'http://127.0.0.1:8000/api/members'