from telegram.ext import Updater, CommandHandler

def start_bot(bot, update):
	my_text = """Привет пользователь!   #Для ввода текста в несколько строк

Я простой бот, который умеет искать информацию.
	
Для начала давайте начнем /start
	"""
	print(update)
	update.message.reply_text(my_text)


def main():
	updtr = Updater("5268755750:AAEcSi0bFuN3DHk1B_euHUQDMfCZSzrgsnc")

	updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
	updtr.start_polling()
	updtr.idle()

if __name__ == "__main__":
	main()

