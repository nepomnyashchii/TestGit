import telebot

bot =telebot.TeleBot("873802609:AAGrF4tID-CD4lufzgMjqNEnqLxhCaEweLM")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.send_message(message.chat.id, message.text)

bot.polling (none_stop = True)