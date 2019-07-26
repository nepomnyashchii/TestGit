import telebot
from telebot import types


bot = telebot.TeleBot("873802609:AAGrF4tID-CD4lufzgMjqNEnqLxhCaEweLM")


@bot.message_handler(content_types=['text'])
def send_echo(message):
     chat_id = message.chat.id
     bot.send_message(chat_id, message.text, parse_mode='HTML',reply_markup=balance_key(chat_id))

def keyboard(btn2=None):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('people')
    btn2 = types.KeyboardButton('water')
    btn3 = types.KeyboardButton("milk")
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    return markup


def balance_key(chat_id):
	keyboard = types.InlineKeyboardMarkup()
	keyboard.add(types.InlineKeyboardButton(text='Go to the main menu',callback_data="message.text"))
	return keyboard

reply_markup = keyboard()

bot.polling(none_stop=True)
