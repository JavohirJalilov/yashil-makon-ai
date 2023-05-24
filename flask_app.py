from flask import Flask, request, jsonify
from telegram import Update, Bot
from settings import TOKEN
from handlers import start, get_location
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
import telegram

app = Flask(__name__)

bot = Bot(TOKEN)

@app.route('/getInfo')
def getInfo():

    info = bot.get_webhook_info()
    return jsonify(info)

@app.route('/set')
def setWebhook():
    
    HOOK_URL = 'https://yashilmakonai.pythonanywhere.com/'
    hook_bool = bot.setWebhook(url=HOOK_URL)
    return str(hook_bool)

@app.route('/', methods=['POST'])
def main():

    dp = Dispatcher(bot, None, workers=1)

    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)

        dp.add_handler(CommandHandler('start', start))
        dp.add_handler(MessageHandler(Filters.location, get_location))

        dp.process_update(update)


    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)