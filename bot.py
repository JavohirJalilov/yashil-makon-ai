from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from settings import TOKEN
from handlers import start, get_location

updater = Updater(TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.location, get_location))

updater.start_polling()
updater.idle()