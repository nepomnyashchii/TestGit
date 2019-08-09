import telebot
import json
import lib
import logger_module
logger = logger_module.setup_logger("flowsapp")

logger.debug("Start Telebot")
bot = telebot.TeleBot("873802609:AAGrF4tID-CD4lufzgMjqNEnqLxhCaEweLM")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    """ print(user_name, user_id, user_fullname, message.text"""
    user = message.from_user
    logger.debug("user: " + str(user))
    user_name = user.username
    logger.debug("user_name: " + str(user_name))
    user_id = user.id
    logger.debug("user_id: " + str(user_id))
    user_fullname = user.first_name + ' ' + str(user.last_name)
    print(user_name, user_id, user_fullname, message.text)



    if (message.text.lower() == 'goodmorning'):
        person = "Alex"
        logger.debug("Start flowdata")
        data = lib.get_flowdata(person, message.text.lower())
        logger.debug("Obtain flowdata")
        content = lib.get_nice_text_from_flows(data)
        logger.debug("Start obtaining information")
        bot.send_message(message.chat.id, content)
        logger.debug("Message to a bot: " + content)

    elif (message.text.lower() == 'good morning'):
        logger.debug("Message to change from good morning to goodmorning in a telegram text")
        bot.send_message(message.chat.id,
                         "Good morning flow for " + str(user_id))

    else:
        bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
