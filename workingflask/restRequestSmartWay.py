import requests

resp = requests.get('http://api.icndb.com/jokes/random')
if resp.status_code != 200:
    # This means something went wrong.
    # raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    print("Ne polucholos'")
    print(resp.status_code)
    

print(resp.json()["value"]["joke"])
