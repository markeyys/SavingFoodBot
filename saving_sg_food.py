import telegram
import logging
import sys

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler, RegexHandler, ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)
logger = logging.getLogger(__name__)



def start(bot, update):

    keyboard = [[InlineKeyboardButton("find by Location", callback_data='1'),
                 InlineKeyboardButton("find by Food", callback_data='2')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        'Hello, welcome to SG find cheap food bot. To start select one of the options below'
        'To quit, end with cancel to leave the bots',
        reply_markup=reply_markup)



def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)



def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("662276798:AAFbFHPtT9I7_sNzKAjKc14XW-b-ZCLT7TU")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))


    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
