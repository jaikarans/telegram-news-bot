from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import CallbackContext
from news_api import api
import urllib.parse


async def search(update: Update, context: CallbackContext.DEFAULT_TYPE):
    if len(context.args) == 0:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       parse_mode=ParseMode.HTML,
                                       text='Invalid argument to command /search please visit /help')

    query_string = ''
    for s in context.args:
        query_string += s
        if context.args.index(s) < len(context.args) - 1:
            query_string += ' '
    url_encoded_query = urllib.parse.quote_plus(query_string)
    data = api.get_everything(language='en', q=url_encoded_query)
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
