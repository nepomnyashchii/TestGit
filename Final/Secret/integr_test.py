import requests

def integration_test():
    response = requests.get(
        "https://5000-c2d101ea-6ebb-45c7-aa95-fd28b9062de9.ws-us0.gitpod.io/secret")
        result = response["sid"]
    if response.status_code !=200:
        return({"error": "wrong status code"})
    else:
        return "Everything is working"

integration_test()
