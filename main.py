import logging

from telegram.ext import ApplicationBuilder, CommandHandler
from handlers import *
from secrets import BOT_KEY

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_KEY).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # /help handler
    help_handler = CommandHandler('help', help)
    application.add_handler(help_handler)

    # /today handler
    today_handler = CommandHandler('today', today)
    application.add_handler(today_handler)

    # /country handler
    today_handler = CommandHandler('country', country)
    application.add_handler(today_handler)

    # /search handler
    search_handler = CommandHandler('search', search)
    application.add_handler(search_handler)

    # /category handler
    category_handler = CommandHandler('category', category)
    application.add_handler(category_handler)

    # /date handler
    date_handler = CommandHandler('date', date)
    application.add_handler(date_handler)

    application.run_polling()
