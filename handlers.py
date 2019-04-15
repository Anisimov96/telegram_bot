
from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler

from db import get_or_create_user, get_or_create_info
from utils import get_keyboard

def greet_user (bot, update, user_data):
    user = get_or_create_user (update.effective_user, update.message)
    print(user)
    text = 'Привет {}'.format(user.username)
    update.message.reply_text(text, reply_markup=get_keyboard())


def anketa_start (bot, update, user_data):
    update.message.reply_text('Давайте заполним таблицу. Напишите ИМЯ человека', reply_markup=ReplyKeyboardRemove())
    return "name"

def anketa_get_name (bot, update, user_data):
    user_name = update.message.text
    update.message.reply_text('Напишите ФАМИЛИЮ человека')
    user_data['anketa_name'] = user_name
    return "surname"

def anketa_get_surname (bot, update, user_data):
    user_surname = update.message.text
    update.message.reply_text('Напишите НОМЕР ТЕЛЕФОНА человека')
    user_data['anketa_surname'] = user_surname
    return "n_phone"

def anketa_get_nomer (bot, update, user_data):
    user_nomer = update.message.text
    update.message.reply_text('Напишите АДРЕС ЭЛЕКТРОННОЙ ПОЧТЫ человека')
    user_data['anketa_nomer'] = user_nomer
    return "n_mail"  

def anketa_get_mail (bot, update, user_data):
    user_mail = update.message.text
    update.message.reply_text('Напишите ДОПОЛНИТЕЛЬНУЮ ИНФОРМАЦИЮ о человеке')
    user_data['anketa_mail'] = user_mail
    return "info"  

def anketa_get_info (bot, update, user_data):
    user_info = update.message.text
    user_data['anketa_info'] = user_info
    info = get_or_create_info(user_data)
    text = 'Данные о {} успешно добавлены в БД'.format(info.surname)
    update.message.reply_text(text, reply_markup=get_keyboard())
    print(info)
    return ConversationHandler.END  

def dontknow (bot, update, user_data):
    update.message.reply_text('Не понимаю!!!')
