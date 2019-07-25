import telebot
from telebot import types

bot = telebot.TeleBot("873802609:AAGrF4tID-CD4lufzgMjqNEnqLxhCaEweLM")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.send_message(message.chat.id, message.text + '?', reply_markup=keyboard())

def keyboard():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	btn1 = types.KeyboardButton('people')
	markup.add(btn1)
	return markup

reply_markup=keyboard()

bot.polling(none_stop=True)



