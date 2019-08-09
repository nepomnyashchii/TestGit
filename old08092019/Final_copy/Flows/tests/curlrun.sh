
# Run to obtain information for news, jokes, cocktail, temperature in a city
# through username

username = Alex
 curl -H "Content-Type: application/json" -X GET http://localhost:5000/run/username/



# Run to obtain information for news, jokes, cocktail, temperature in a city
# through username and flow
username = Alex
flow = goodmorning
curl -H "Content-Type: application/json" -X GET http://localhost:5000/run/username/flow
