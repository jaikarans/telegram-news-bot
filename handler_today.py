from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import CallbackContext
from news_api import api


async def today(update: Update, context: CallbackContext.DEFAULT_TYPE):
    data = api.get_top_headlines(language='en', country='in')
    newsCount = 0
    for news in data['articles']:
        newsCount += 1
        if newsCount > 20:
            break
        count = '<b>' + str(newsCount) + '</b>'
        if news['urlToImage'] is not None:
            msg = count + ' <a href="' + news['url'] + '"><b>' + news['title'] + '</b></a>'
            await context.bot.send_photo(chat_id=update.effective_chat.id,
                                         photo=news['urlToImage'],
                                         parse_mode=ParseMode.HTML, caption=msg)
        else:
            msg = count + ' <a href="' + news['url'] + '"><b>' + news['title'] + '</b></a>'
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text=msg,
                                           parse_mode=ParseMode.HTML)
