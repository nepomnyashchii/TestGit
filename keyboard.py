import telebot
from telebot import types
from config import token
from poloniex import api_query

bot = telebot.Telebot(token)

@bot.message_handler(commands = ['start']
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        '''Good morning''',
        reply_markp =keyboard())

@bot.message_handler(content_types = ["text"])
def send_anytext(message):
    chat_id = message.chat.id
    if message.text == "Balance":
        text = "Yout balance \n\n"
        balance = api_query('returnBalances'
        for i in balance.items():
            if i[1] != '0.000000':
                print(i)
                text = text + '<b>' + i[0] + '</b>' + '\t --- \t' + i[1] + '\n'
        bot.send_message(chat_id, text, parse_mode = 'HTML', reply_markup = keybooard())

def keyboard ():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard = True)
    btn1 = types.KeyboardButton('Balance')
    markup.add(btn1)
    return markup

if __name__ == " __main__":
    bot.polling(none_stop=True)

