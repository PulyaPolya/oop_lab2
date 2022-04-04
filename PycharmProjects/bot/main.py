import telebot
from telebot import types
from random_word import RandomWords
#import j
import test
import tree

root = test.fill_the_tree()
last_letters=[]
bot=telebot.TeleBot('5139021734:AAEn6NEowa45V30tb2rBliZUTrEIpiv6O7M')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Enter any capital )')
    #markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #item1 = types.KeyboardButton("Hint")
    #markup.add(item1)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Hint")
    markup.add(item1)
    bot.send_message(m.chat.id, 'Press "Hint" to get the first letter of capital',
                     reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip()=='Hint':
        if last_letters:
            result=test.find_word(test.root,last_letters[-1],0 )
            if result[0] !='NONE':
                bot.send_message(message.chat.id, result[0][0]+result[0][1] +' ('+ result[0]+ ')')
                tree.inorder(test.root)
            else:
                bot.send_message(message.chat.id, "You've lost ):")
                test.root = test.fill_the_tree()
                last_letters.clear()
        else:
            bot.send_message(message.chat.id, last_letters[-1] + 'tirana')
    else:
        user_word=message.text.lower()

        answer = test.check_input(user_word, test.root)
        tree.inorder(test.root)
        if answer[0]=='ok' and test.check_user_first_letter(last_letters, user_word)== 'ok':

            root=answer[1]
            last_character = user_word[-1]
            result=test.find_word(root, last_character,1)
            bot_word=result[0]
            root=result[1]

            if bot_word!='NONE':
                bot.send_message(message.chat.id,bot_word)
                test.root=root
                last_letters.append(bot_word[-1])
            else:
                bot.send_message(message.chat.id, "I've lost ):" )
                test.root=test.fill_the_tree()
                last_letters.clear()

        else:
            bot.send_message(message.chat.id, "You've lost ):")
            test.root = test.fill_the_tree()
            last_letters.clear()
bot.polling(none_stop=True, interval=0)
