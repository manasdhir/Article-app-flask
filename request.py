import requests
data = {
    'email':"asdsafasf@gmail.com"
}
headers = {
    'Content-Type': 'application/json'
}

response_get=requests.put("http://127.0.0.1:8000/api/user/dsgsags",json=data,headers=headers)
print(response_get.json())