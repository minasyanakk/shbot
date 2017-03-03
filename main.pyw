# -*- coding: utf-8 -*-
import os
import telebot
from telebot import types
import urllib2, base64
import rout
token = '330827513:AAGP_l173M7BZNCbpibSK-rw-SWT0r-ZnMc'


bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
	markup = types.ReplyKeyboardMarkup()
	markup.row('shutdown','shutdown 1 hour','reboot','reboot router')
	if message.text=='shutdown':
		f = os.system("shutdown -s -t 1")
		bot.send_message(message.chat.id, "Выключайю", reply_markup=markup)
	elif message.text == 'shutdown 1 hour':
		s = os.system("shutdown -s -t 3600")
		bot.send_message(message.chat.id, "Хорошо, через час выключу!", reply_markup=markup)
	elif message.text == 'reboot':
		s = os.system("shutdown -r")
		bot.send_message(message.chat.id, "Перезагружаю", reply_markup=markup)
	elif message.text == 'reboot router':
		w = rout.rerout()
		bot.send_message(message.chat.id, "Перезагружаю", reply_markup=markup)
print "bot telegram working!"
if __name__ == '__main__':
     bot.polling(none_stop=True)

