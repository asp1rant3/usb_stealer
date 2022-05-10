import telebot

def sendLinkToChat(link: str, chat=СЮДА ВСТАВЛЯЕМ ВАШ ID, token="СЮДА ТОКЕН БОТА") -> None:
	bot = telebot.TeleBot(token=token)
	bot.send_message(chat_id=chat, text=link)