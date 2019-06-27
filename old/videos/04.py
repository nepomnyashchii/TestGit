import pyowm
city = input("What is is weather in: ?")
API_key = '1bdcae6b7d23f180361c8878a965c9f8'
owm = pyowm.OWM(API_key)
observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature = w.get_temperature('celsius')['temp']
print("In " + city + " temperature now is: " + str(temperature) + " degrees celcius")
print("In our city " + w.get_detailed_status())



