from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import CallbackContext

async def help(update: Update, context: CallbackContext.DEFAULT_TYPE):
    intro = 'This messages tells you how to use this bot\n\n'
    helps = '/help - see this message\n'
    today = '/today - see today\'s top highlighs\n'
    country = '/country <b>country_code</b> - see the top highlights of the country\n<i><b>ex</b> - /country in</i>\n'
    category = '/category <b>category_name</b> - find the news according to category\n<i><b>ex</b> - /category sports</i>\n'
    search = '/search <b>query_keywords</b> - search the news according to keywords\n<i><b>ex</b> - /search russia ukraine</i>\n'
    date = '/date <b>yyyy-mm-dd query_keyword</b> - search news for a previous date, not older than 1 month. and query_keyword also required\n'
    date_example = '<i><b>ex</b> - /date 2022-05-28 ukraine</i>\n'
    msg = intro + helps + today + country + category + search + date + date_example
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   parse_mode=ParseMode.HTML,
                                   text=msg)
