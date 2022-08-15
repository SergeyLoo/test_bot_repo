# This is a sample Python BOT.
# тестовый бот для студии танцев Soul Space

import telebot;

bot = telebot.TeleBot('5586138889:AAE8YoxT4pzI_NINMtQN3cP2QttnCU5Bg6k', parse_mode = None);

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, 'Привет, чем я могу тебе помочь?')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши привет')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши /help.')

bot.polling(none_stop = True, interval=0)




