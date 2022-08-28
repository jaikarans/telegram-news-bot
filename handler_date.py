from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import CallbackContext
from news_api import api
import datetime

categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']


async def date(update: Update, context: CallbackContext.DEFAULT_TYPE):
    if len(context.args) != 2:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       parse_mode=ParseMode.HTML,
                                       text='Invalid argument to command /date please visit /help')

    date_format = '%Y-%m-%d'
    try:
        datetime.datetime.strptime(context.args[0], date_format)
    except ValueError:
        msg = "<b>Invalid date format!!</b>\n \
              try <b>YYYY-MM-DD</b> or <b>DD-MM-YYYY</b> formats"
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=msg,
                                       parse_mode=ParseMode.HTML)
        return

    data = api.get_everything(language='en', from_param=context.args[0], q=context.args[1])
    if len(data['articles']) == 0:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text='news for this date and query combination is available')
        return
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
