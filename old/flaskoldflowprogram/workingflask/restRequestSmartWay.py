import requests
print(requests)

resp = requests.get('http://api.icndb.com/jokes/random/?lastName=Doe&firstName=Mike1')
if resp.status_code != 200:
    # This means something went wrong.
    # raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    print("Ne polucholos'")
    print(resp.status_code)


print(resp.json()["value"]["joke"])
