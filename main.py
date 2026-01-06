import requests
# this line is important, it allows you to make requests

print("hello internet")

response = requests.get("https://catfact.ninja/fact")
# this is the address and request being made

print(response.status_code)
# 200 means its working

print(response.json())
# if its a JSON API, this is how it be
# JSON = Javascript Object Notation I think its like some format of the response 
# (the thing being printed here is a dictionary btw: a list of variables and corresponding values)

print(response.json()['fact'])
# this prints out the specific value of the variable named "fact"


