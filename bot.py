import os
from telegram import Bot
from flask import Flask, request

app = Flask(__name__)

# Ambil token dan chat ID dari environment variable
bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")

bot = Bot(token=bot_token)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get('message', 'Alarm TradingView!')
    bot.send_message(chat_id=chat_id, text=message)
    return "OK", 200

if __name__ == '__main__':
    app.run(debug=True)
