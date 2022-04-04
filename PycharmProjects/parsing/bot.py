import telebot
from telebot import types

import scraper

bot=telebot.TeleBot('5171973743:AAHO0NNVXN_nx_Bmn4GdT0ZB42DDFqi5b1E')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    #bot.send_message(m.chat.id, 'I can tell you current temperature')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Tell temperature")
    markup.add(item1)
    item2 = types.KeyboardButton("Tell how it feels")
    markup.add(item2)
    bot.send_message(m.chat.id, 'I can tell you current temperature',reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip()=="Tell temperature":
        temperature=scraper.get_weather()
        bot.send_message(message.chat.id, temperature)
    elif message.text.strip()=="Tell how it feels":
        temperature=scraper.get_how_it_feels()
        bot.send_message(message.chat.id, temperature)
bot.polling(none_stop=True, interval=0)
