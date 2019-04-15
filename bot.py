
from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler, ConversationHandler, Filters

import settings
from handlers import*


def main():
    mybot=Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    dp = mybot.dispatcher

    # Обработчик команды /start
    dp.add_handler(CommandHandler('start', greet_user, pass_user_data=True))

   
    # Добавим диалог (запись информации в БД)
    anketa = ConversationHandler(
        entry_points = [RegexHandler('^(Добавить данные в БД)$', anketa_start, pass_user_data=True)],
        states = {
            "name":[MessageHandler(Filters.text, anketa_get_name, pass_user_data=True)],
            "surname": [MessageHandler(Filters.text, anketa_get_surname, pass_user_data=True)],
            "n_phone": [MessageHandler(Filters.text, anketa_get_nomer, pass_user_data=True)],
            "n_mail": [MessageHandler(Filters.text, anketa_get_mail, pass_user_data=True)],
            "info": [MessageHandler(Filters.text, anketa_get_info, pass_user_data=True)]
        },
        fallbacks = [MessageHandler(Filters.text, dontknow, pass_user_data=True)]
    )
    dp.add_handler(anketa)

    '''# Обработчик вх.сообщений (достает информацию из БД)
    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))'''

    mybot.start_polling()
    mybot.idle()

main()