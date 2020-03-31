import telebot
import requests
import json
import datetime
import json
import os

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	chat_id = message.from_user.id
	action_string = 'typing'
	bot.send_chat_action(chat_id, action_string)

	mensaje = """Hey, hola! Yo soy Alana, el asistente virtual de los trabajadores de Telmex. Estoy aquí para ayudarte. 
	Yo te estaré enviando distintos tipos de notificaciones.
	
	También puedo brindarte tu <b>Telegram_id</b>, sólo envíame el comando: /obtener_id_telegram y te lo estaré enviando.
	Si tienes algún problema, se lo podrías reportar al equipo de Inovación tecnológica o a @iangelmx."""

	bot.reply_to(message, mensaje, parse_mode='HTML')

@bot.message_handler(commands=['obtener_id_telegram'])
def comando(message):
	chat_id = message.from_user.id
	
	mensaje="Tu Telegram id es:\n\n<b>"+str(chat_id)+"</b>"

	bot.reply_to(message, mensaje,  parse_mode='HTML')

bot.polling()

while True: # Don't let the main Thread end.
	pass

