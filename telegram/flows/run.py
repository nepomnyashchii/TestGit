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
    person ="Alex"
    flow ="goodmorning"
    data = lib.get_flowdata(person, flow)
    print(data)
    if not data:
        return  "Error = no data for this user and flow"
    simple_list = []
    for idx, line in enumerate(data):
        actionline = line[0]
        if (message.text == 'great'):
            action_data = lib.run_action(actionline)
            text = action_data
            bot.send_message(message.chat.id, text)
        elif (message.text == "good night"):
            bot.send_message( message.chat.id, "Good morning flow for " + str(user_id))
        else:
            bot.send_message(message.chat.id, message.text)
bot.polling(none_stop=True)

