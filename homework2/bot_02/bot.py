import settings
import logging
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename='bot.log', level=logging.INFO)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Бот 2 стартовал")
    mybot.start_polling()
    mybot.idle()


def greet_user(update, context):
    ok_flag = True
    date = '2020/11/30'
    if context.args:
        try:
            my_planet = context.args[0]
            message = f"Название планеты: {my_planet}"
            try:
                ephem_planet = getattr(ephem, my_planet)
                planet_date = ephem_planet(date)
                constellation = ephem.constellation(planet_date)
                message = f"Ответ: планета находится в : {constellation}"
            except (TypeError, ValueError):
                message = "Введите правильное название планеты"
        except (TypeError, ValueError):
            message = "Введите название планеты. Ошибка в типе"
    else:
        message = "Введите название планеты"
    update.message.reply_text(message)

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text("Я Бот, отвечаю тем же: " + user_text)

if __name__ == "__main__":
    main()