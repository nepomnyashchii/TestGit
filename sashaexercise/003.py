import requests
a= "Please provide me wih some information about NASA:"
r =  requests.get("https://api.nasa.gov/planetary/apod?api_key=NNKOjkoul8n1CH18TWA9gwngW1s1SmjESPjNoUFo")
print(a)
print(r.content)