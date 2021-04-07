import os
import requests
import json
AUTH_ENDPOINT='http://127.0.0.1:8000/api/user/register/'

headers={
    "Content-Type":"application/json",
}

data={
    'username':"newuser1",
    'email': "newuser1@gmail.com",
    'password': "newuser123",
    'password2': "newuser123",
}
r=requests.post(AUTH_ENDPOINT,data=json.dumps(data),headers=headers)
token=r.json()
print(token)