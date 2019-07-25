import telebot
import pyowm
from telebot import types


bot =telebot.TeleBot("873802609:AAGrF4tID-CD4lufzgMjqNEnqLxhCaEweLM")


@bot.message_handler(content_types=['text'])
def send_echo(message):

    API_key = '1bdcae6b7d23f180361c8878a965c9f8'
    owm = pyowm.OWM(API_key)
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temperature = w.get_temperature('celsius')['temp']
    answer = "In " + message.text + " temperature now is: " + str(temperature) + " degrees celcius" + "\n"
    answer +="In our city " + w.get_detailed_status()
    apple = "no such city"
    if len(message.text)>0:
        return bot.send_message(message.chat.id, answer, reply_markup=keyboard())
    else:
        return "No such city"

def keyboard():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	btn1 = types.KeyboardButton('Brooklyn')
	markup.add(btn1)
	return markup

reply_markup=keyboard()



bot.polling (none_stop = True)