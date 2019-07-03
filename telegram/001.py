import telebot
import json
import lib

bot = telebot.TeleBot("873802609:AAGrF4tID-CD4lufzgMjqNEnqLxhCaEweLM")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    user = message.from_user
    user_name = user.username
    user_id = user.id
    user_fullname = user.first_name + ' ' + user.last_name
    print(user_name, user_id, user_fullname, message.text)

    if (message.text.lower() == 'todo'):
        data = lib.get_all()
        text = ''
        for todo in data:
            text += todo["text"]
            if todo["done"] != 0:
                text += ' - Done\n'
            else:
                text += '\n'
        print(text)
        bot.send_message(message.chat.id, text)
    elif (message.text == 'Flow'):
        bot.send_message(message.chat.id, "What Flow u want to run")
    else:
        bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
