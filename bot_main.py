import telebot;
bot = telebot.TeleBot('5656158526:AAG-oligizH1R67E8EQd0i1hBOg3dCl6NZE');
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "Привет":
      bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе погоду на сегодня.")
  elif message.text == "/help":
      bot.send_message(message.from_user.id, "Напиши Привет")
  else:
      bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)
# # Готовим кнопки
# keyboard = types.InlineKeyboardMarkup()
# # По очереди готовим текст и обработчик для каждого знака зодиака
# key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac')
# # И добавляем кнопку на экран
# keyboard.add(key_oven)
# key_telec = types.InlineKeyboardButton(text='Телец', callback_data='zodiac')
# keyboard.add(key_telec)
# key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac')
# keyboard.add(key_bliznecy)
# key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')
# keyboard.add(key_rak)
# key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')
# keyboard.add(key_lev)
# key_deva = types.InlineKeyboardButton(text='Дева', callback_data='zodiac')
# keyboard.add(key_deva)
# key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='zodiac')
# keyboard.add(key_vesy)
# key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac')
# keyboard.add(key_scorpion)
# key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac')
# keyboard.add(key_strelec)
# key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac')
# keyboard.add(key_kozerog)
# key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac')
# keyboard.add(key_vodoley)
# key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac')
# keyboard.add(key_ryby)
# # Показываем все кнопки сразу и пишем сообщение о выборе
# bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)