# telegram_echo_bot.py
# A simple Telegram bot that replies with the same message you send
# Author: somtexy

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Replace this with your BotFather token
TELEGRAM_TOKEN = "YOUR_BOT_TOKEN_HERE"

# Start command
def start(update, context):
    update.message.reply_text("Hello 👋! I’m alive and ready.")

# Echo back user messages
def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
