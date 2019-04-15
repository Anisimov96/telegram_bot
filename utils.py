from telegram import ReplyKeyboardMarkup

# функция обновления клавиатуры (не привязана к /start)
def get_keyboard ():
    my_keyboard = ReplyKeyboardMarkup([['Добавить данные в БД']], resize_keyboard=True)
    return my_keyboard