import telegram
import logging
import sys
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler, RegexHandler, ConversationHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup, ReplyKeyboardRemove


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)
logger = logging.getLogger(__name__)







def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)



def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("662276798:AAFbFHPtT9I7_sNzKAjKc14XW-b-ZCLT7TU")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher



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
