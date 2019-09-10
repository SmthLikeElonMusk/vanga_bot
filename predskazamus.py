import telebot
import random

bot = telebot.TeleBot('902235559:AAFNVuIYnvg_g7CK_s8LP1hecosJJGjpjps')

@bot.message_handler(commands = ['start'])
def start(message):
	bot.send_message(message.chat.id, 'Привет! Я бот-предсказамус, задавай вопросы!')

@bot.message_handler(content_types = ['text'])
def predskazanie(message):
	a = random.randint(0, 8)
	if a == 0:
		bot.send_message(message.chat.id, 'Да!')

	elif a == 1:
		bot.send_message(message.chat.id, 'Нет')

	elif a == 2:
		bot.send_message(message.chat.id, 'Возможно...')

	elif a == 3:
		bot.send_message(message.chat.id, 'Кто знает...')

	elif a == 4:
		bot.send_message(message.chat.id, 'Стоит попробовать')

	elif a == 5:
		bot.send_message(message.chat.id, 'Абсолютно точно')

	elif a == 6:
		bot.send_message(message.chat.id, 'Я хз. Я просто программа, которую запихнули в этого бота. Чем ты занимаешся?!')

	elif a == 7:
		bot.send_message(message.chat.id, 'Вангую... Вернусь не скоро')

	elif a == 8:
		bot.send_message(message.chat.id, 'Мож рискнуть')

bot.polling()



