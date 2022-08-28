from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import CallbackContext
from news_api import api

categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']

async def category(update: Update, context: CallbackContext.DEFAULT_TYPE):
    if len(context.args) != 1:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       parse_mode=ParseMode.HTML,
                                       text='Invalid argument to command /category please visit /help')

    query_string = ''
    if context.args[0] not in categories:
        msg = 'Sorry This category is not defined in our app \n \
            try one of these Categories : \
            <b> business, entertainment, general, health, science, sports, technology</b>'
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=msg,
                                       parse_mode=ParseMode.HTML)
        return

    data = api.get_top_headlines(language='en', category=context.args[0])
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
