import telegram
import logging

import json
import requests

from telegram import message
import sys
from get_new_query import DBQuery

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler, RegexHandler, \
    ConversationHandler, CallbackQueryHandler

from telegram.ext import *

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


TOKEN = "662276798:AAFbFHPtT9I7_sNzKAjKc14XW-b-ZCLT7TU"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):

    keyboard = [[telegram.KeyboardButton("Find by Location", request_location=True),
                 telegram.KeyboardButton("/Find_by_Food")]]

    reply_markup = telegram.ReplyKeyboardMarkup(keyboard)

    bot.send_message(chat_id=update.message.chat_id,
                     text='Hello, welcome to SG find cheap food bot. To start select one of the options below \n' 
                          'To quit, end with cancel to leave the bots',
                     reply_markup=reply_markup)


def location(bot, update):
    # print ("testing")
    print(update.message.location)


def button(bot, update):
    query = update.callback_query

    bot.edit_message_text(text="Selected option: {}".format(query.data),
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)


def find_by_food(bot, update):
    update.message.reply_text("Hot Search: \n"
                              "1) ChickenRice \n"
                              "2) DuckRice \n"
                              "Or \n"
                              "Type your own")


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return text, chat_id


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def search_by_name(bot, update):
    print("hello")
    text, chat = get_last_chat_id_and_text(get_updates())
    print(text)
    send_message(text, chat)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the EventHandler and pass it your bot's token.
    # 662276798:AAFbFHPtT9I7_sNzKAjKc14XW-b-ZCLT7TU
    updater = Updater("662276798:AAFbFHPtT9I7_sNzKAjKc14XW-b-ZCLT7TU")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("Find_by_Food", find_by_food))
    dp.add_handler(CommandHandler("searchFood", search_by_name))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(MessageHandler(Filters.location, location))

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
