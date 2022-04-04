import telebot
from telebot import types
import messanger
from enum import Enum
import ini_file
parameters= ['mark', 'sport', 'instagram', 'everything']
class State(Enum):
    wait_for_tr=1
    wait_for_mark=2
    nothing=0
    wait_for_change = 3
    wait_for_sport = 4
    wait_for_inst=5
bot_mes=messanger.Messanger()
#bot_mes.dick_tr=ini_file.fill_dict()
def edit_arr(arr):
    line=''
    for elem in arr:
        line+=elem
        line+='\n'
    return line
bot=telebot.TeleBot('5138455027:AAEjzwHCqd08Pc8iTyxygrJLarwLtrqQZ4M')
def get_list(message):
    arr = bot_mes.get_trainers()
    markup_inline = types.InlineKeyboardMarkup()
    for elem in arr:
        item = types.InlineKeyboardButton(text=elem, callback_data=elem)
        markup_inline.add(item)
    bot.send_message(message.chat.id, 'Please choose the name of trainer', reply_markup=markup_inline)
@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Add trainer")
    markup.add(item1)
    #item2 = types.KeyboardButton("Tell how it feels")
    #markup.add(item2)
    bot.send_message(m.chat.id, 'I can tell you current temperature',reply_markup=markup)
@bot.message_handler(commands=['addtrainer'])
def tr(message):
    bot.send_message(message.chat.id, 'Please enter the name of trainer')
    bot_mes.state=State.wait_for_tr
@bot.message_handler(commands=['set'])
def set(message: types.Message):
    get_list(message)
    bot_mes.command = 'set'
@bot.message_handler(commands=['get'])
def get(message: types.Message):
    get_list(message)
    bot_mes.command='get'
@bot.callback_query_handler(func=lambda call: call.data in bot_mes.get_coaches_name())
def choose(call):
    message='What do you want to set or get for ' + call.data + '?'
    bot_mes.current_coach_name=call.data
    markup_inline = types.InlineKeyboardMarkup()
    for parameter in parameters:
        item=types.InlineKeyboardButton(text=parameter, callback_data=parameter)
        markup_inline.add(item)
    bot.send_message(call.from_user.id, message, reply_markup=markup_inline)
@bot.callback_query_handler(lambda first:first.data in parameters and bot_mes.command == 'set')
def answer(call):
    if call.data=='mark':
        bot_mes.state = State.wait_for_mark
        bot.send_message(call.from_user.id, 'Please enter a mark for ' + bot_mes.current_coach_name)
    elif call.data=='sport':
        bot_mes.state = State.wait_for_sport
        markup_inline = types.InlineKeyboardMarkup()
        for sport in bot_mes.list_of_sports:
            item = types.InlineKeyboardButton(text=sport, callback_data=sport)
            markup_inline.add(item)
        item = types.InlineKeyboardButton(text='add new sport', callback_data='add')
        markup_inline.add(item)
        bot.send_message(call.from_user.id,'Please choose a sport for ' + bot_mes.current_coach_name + ' or add a new one', reply_markup=markup_inline)
    elif call.data=='instagram':
        bot_mes.state=State.wait_for_inst
        bot.send_message(call.from_user.id, 'Please enter an instagram for ' + bot_mes.current_coach_name)
@bot.callback_query_handler(lambda first:first.data in parameters and bot_mes.command == 'get')
def answer(call):
    coach = bot_mes.get_coach(bot_mes.current_coach_name)
    if call.data=='mark':
        bot.send_message(call.from_user.id, 'Mark for ' + bot_mes.current_coach_name+ ' is ' + coach.mark)
    elif call.data=='sport':
        index= int(coach.sport)
        bot.send_message(call.from_user.id, 'Sport for ' + bot_mes.current_coach_name + ' is ' + bot_mes.list_of_sports[index])
    elif call.data=='instagram':
        bot.send_message(call.from_user.id, 'Instagram for ' + bot_mes.current_coach_name + ' is ' +coach.instagram)

@bot.callback_query_handler(lambda first:first.data in bot_mes.list_of_sports )
def answer(call):
    coach = bot_mes.get_coach(bot_mes.current_coach_name)
    coach.sport=bot_mes.list_of_sports.index(call.data)
    bot.send_message(call.from_user.id, 'We set ' + call.data+' for '+bot_mes.current_coach_name)
@bot.callback_query_handler(lambda first:first.data =='add')
def answer(call):
    bot_mes.state = State.wait_for_sport
    bot.send_message(call.from_user.id, 'Please enter any sport')
@bot.message_handler(commands=['save'])
def mark(message):
    ini_file.update_info(bot_mes.coaches, bot_mes.list_of_sports)
    bot.send_message(message.chat.id, 'We saved your info successfully')
@bot.message_handler(commands=['addsport'])
def add_sport(message):
    bot_mes.state=State.wait_for_sport
    bot.send_message(message.chat.id, 'Please enter any sport')
@bot.callback_query_handler(func=lambda call:True)
def answer(call):
    coach = bot_mes.get_coach(bot_mes.current_coach_name)
    coach.sport=call.data
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if bot_mes.state.value==State.wait_for_tr.value:
        coach=bot_mes.get_coach(message.text.strip())
        bot.send_message(message.chat.id, 'Please now rate this trainer')
        bot_mes.state=State.wait_for_mark
        bot_mes.current_coach_name=coach.name
    elif bot_mes.state.value==State.wait_for_mark.value:
        if message.text.strip().isnumeric() and int(message.text.strip())<=10 and int(message.text.strip())>=0:
            coach = bot_mes.get_coach(bot_mes.current_coach_name)
            #bot_mes.add_to_mark(bot_mes.current_trainer,message.text.strip())
            coach.mark=message.text.strip()
            bot_mes.state=State.nothing
        else:
            
            bot.send_message(message.chat.id, 'Please enter the correct mark')
    elif bot_mes.state.value==State.wait_for_sport.value:
        sport_already_exists = 0
        for sport in bot_mes.list_of_sports:
            if sport == message.text.strip():
                sport_already_exists = 1
        if sport_already_exists == 0:
            bot_mes.list_of_sports.append(message.text.strip())
        else:
            bot.send_message(message.chat.id, 'Sorry,this sport is already in the list')
    elif bot_mes.state.value==State.wait_for_inst.value:
        coach = bot_mes.get_coach(bot_mes.current_coach_name)
        coach.instagram=message.text.strip()
bot.polling(none_stop=True, interval=0)
