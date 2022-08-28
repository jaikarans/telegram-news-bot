from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import CallbackContext

async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
    msg = 'hi <b>'+update.message.from_user.name+'</b>, Welcome to the news boot.Here you can read news from 51 countries.'\
        +'\nplease type /help for see the use of this boot'
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   parse_mode=ParseMode.HTML,
                                   text=msg)
