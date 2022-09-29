import telebot
from telebot import types

bot = telebot.TeleBot('5757492065:AAF-9MM93Sq0q98KnVfT-DgI39HNU9JZP_4')


@bot.message_handler(commands=['instagram'])
def instagram(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Перейти в Инстаграм", url="https://instagram.com/anninails_minsk?igshid=YmMyMTA2M2Y="))
	bot.send_message(message.chat.id, "Нажмите на кнопку ниже,чтобы посмотреть работу мастера", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton('💬 Написать мне')
	item2 = types.KeyboardButton('💅 Мои работы ')
	item3 = types.KeyboardButton(' 💵 Прайс на услугу')
	markup.add(item1, item2, item3)
	bot.send_message(message.chat.id, 'Привет!Используйте кнопки под текстом 👇 '.format(message.from_user), reply_markup=markup, parse_mode='html')


@bot.message_handler(content_types=['text'])
def text(message):
	chat_id = message.chat.id
	if message.chat.type == 'private':
		if message.text == 'Отправить мне сообщение':
			bot.send_message(chat_id=1479090626, text='💅  :')
			bot.register_next_step_handler_by


		elif message.text == 'Мои работы':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton('Перейти')
			back = types.KeyboardButton('⬅️ Назад')
			markup.add(item1, back)

			bot.send_message(message.chat.id, "Нажмите на кнопку ниже,чтобы посмотреть работу мастера", parse_mode='html', reply_markup=markup)


		elif message.text == '💵 Прайс на услугу':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton('Маникюр + гель-лак - 30р.')
			item2 = types.KeyboardButton('Маникюр + френч - 35р.')
			item3 = types.KeyboardButton('Наращивание- 40р.')
			item4 = types.KeyboardButton('Маникюр без покрытия-20р.')
			back = types.KeyboardButton('⬅️ Назад')
			markup.add(item1, item2, item3, item4,  back)

			bot.send_message(message.chat.id, '💵 Прайс на услугу', reply_markup=markup)


		elif message.text == '⬅️ Назад':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton('💬 Написать мне')
			item2 = types.KeyboardButton('💅 Мои работы ')
			item3 = types.KeyboardButton(' 💵 Прайс на услугу')

			markup.add(item1, item2, item3)

			bot.send_message(message.chat.id, '⬅️ Назад', reply_markup=markup)


bot.polling(none_stop=True)

