from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import CallbackContext
from news_api import api
from available_countries import country_dict


# function for /country command
async def country(update: Update, context: CallbackContext):
    if len(context.args) != 1:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       parse_mode=ParseMode.HTML,
                                       text='Invalid argument to command /country please visit /help')

    if context.args[0] not in country_dict:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       parse_mode=ParseMode.HTML,
                                       text='<b>Sorry!</b> either we are not available in the country you entered\
                                            <b>or</b> you have entered wrong country code')
        return

    data = api.get_top_headlines(language='en', country=context.args[0])

    if len(data['articles']) == 0:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       parse_mode=ParseMode.HTML,
                                       text='sorry right now no news from ' + context.args[0] + '(<b>'
                                            + country_dict.get(context.args[0]) + '</b>)')
        return

    newsCount = 0
    for news in data['articles']:
        newsCount += 1
        if newsCount > 20:
            break
        # print(newsCount, ' ', news['title'], " ", news['url'])
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
