from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import matplotlib.pyplot as plt
from PIL import Image
import cv2
import os


api_key = 'AIzaSyAGbq62NbISl1Z5of3rchhA_dG_HYmGfQs'

from get_image import get_image
from preprocess import preprocess

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text="Send a location",
    )

def get_location(update: Update, context: CallbackContext) -> None:
    bot= context.bot 
    chat_id = update.message.chat.id 
    # text = update.message.text 
    longitude  = update.message.location.longitude 
    latitude = update.message.location.latitude 
    
    image = get_image(api_key,longitude,latitude,19)
    image = preprocess(image)
    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    cv2.imwrite('map.png', image)
    image = open('map.png', 'rb')
    # os.remove('map.png')
    bot.send_photo(chat_id=chat_id, photo=image)
    

updater = Updater('1925798170:AAEhdke3ALP-riQJ2diNyoQWkUSWLWeTm1o')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.location, get_location))

updater.start_polling()
updater.idle()