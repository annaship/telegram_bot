#!/usr/bin/python3
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Changed from the Echo example by A. Shipunova Aug 2022 
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import shlex, subprocess
import os, sys 
import logging
import unicodedata

from turtle import up

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    logger.info(update)
    logger.info("username = " + update.effective_user.name)
    blacklist = ['@demonsterz', '@AnyaShip3'] 
    
    if not update.effective_user.name in blacklist:
      user = update.effective_user
      update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
          reply_markup=ForceReply(selective=True),
      )

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help me!')

def echo_command(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    logger.info(update)
    update.message.reply_text(update.message.text)

def send2wiki(update: Update, context: CallbackContext) -> None:
    """Send to wiki the user message."""
    logger.info(update.effective_user.name)
    blacklist = ['@demonsterz']
    if not update.effective_user.name in blacklist:
      msg_id = str(update.message.message_id) 
      text2send = msg_id + " ## " + update.message.text
      text2send = text2send.replace("'", "\\'").replace('"', '\\"')
      text2send = unicodedata.normalize('NFC', text2send)
      cmd = 'python3 /home/rubikus/software/bots/print_to_wiki.py ' + text2send
      # print("CMD: %s" % cmd)
      args2send = shlex.split(cmd)

      p = subprocess.run(args2send)

    #TODO: change to a function 
    if update.effective_user.name in blacklist:
      msg_id = str(update.message.message_id) 
      logger.info("message_id %s, bad username %s", msg_id, update.effective_user.name) 
      context.bot.deleteMessage (message_id = update.message.message_id,
                             chat_id = update.message.chat_id)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(sys.argv[1])

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - send the message to Wiki
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, send2wiki))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

