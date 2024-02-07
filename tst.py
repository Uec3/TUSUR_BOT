from tusur import Timetable
import telebot

# bot = telebot.TeleBot('6739938663:AAEyBf4oSs468ss55Isryo64Sd4loE_duwc')

# @bot.message_handler(commands=['start'])
# def main(message):
    # bot.send_message(message.chat.id, )
timetable = Timetable()
# buttonMonday = types.InlineKeyboardButton(,)     
for day in timetable.get_timetable("362-4",week_id = 704 ):
    # bot.send_message(message.chat.id, str(day.get('day')))
    print(day.get('day'))
    for lesson in day.get('lessons'):
        if(lesson.get('discipline') != None):
            print('\t',lesson.get('time'),lesson.get('discipline'),lesson.get('kind'), lesson.get('teacher'))
# bot.polling(none_stop=True)
                