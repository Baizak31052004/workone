import telebot

bot = telebot.TeleBot('6137537431:AAGQ4QRxm-ora8ItDVH5AWDqSqn8ZbUFyG4')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, "И тебе привет", parse_mode='html')
    elif message.text == "Клуб программистов":
        bot.send_message(message.chat.id, f"салам всем вы самые лучшие{message.from_user.id} ", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
        
    else:
        bot.send_message(message.chat.id, "Я тебя не понял", parse_mode='html')


bot.polling(none_stop=True)