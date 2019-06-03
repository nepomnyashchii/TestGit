import requests
a= "Please provide me with one of the random jokes :"
r =  requests.get('http://api.icndb.com/jokes/random/1')
print(a)
print(r.content)



