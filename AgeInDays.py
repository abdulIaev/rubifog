import telebot, time

bot = telebot.TeleBot('1254795383:AAE--Iq_7a_NNFev4NZxoFZJcsQ1B5ZQHLU', parse_mode='HTML')

@bot.message_handler(commands=['start'])

def start(message):
	bot.send_message(message.chat.id, 'Привет {0}, скажи сколько тебе лет в цифрах?'.format(message.from_user.first_name))
	bot.register_next_step_handler(message, age_step)

def age_step(message):
	age = message.text

	if not age.isdigit():

		bot.send_message(message.chat.id, 'Введите <b>только цифрами</b> ваш возраст')
		bot.register_next_step_handler(message, age_step)
	
	else:
		result = (int(age) * 365) + (int(age) // 4)
		bot.send_message(message.chat.id, '{0}: Со дня твоего рождения прошло {1} дней'.format(time.strftime('%D %H:%M:%S'), result))

bot.polling()