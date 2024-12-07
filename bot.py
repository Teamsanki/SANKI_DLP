import logging
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import InputMediaPhoto

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot Token from your BotFather
TOKEN = os.getenv("7908847221:AAFo2YqgQ4jYG_Glbp96sINg79zF8T6EWoo")

# Start command
def start(update: Update, context: CallbackContext) -> None:
    welcome_msg = "Welcome to the Music Bot! This bot will help you deploy and host your bot on GitHub."
    update.message.reply_text(welcome_msg)
    # Send a welcome image
    update.message.reply_media_group([InputMediaPhoto('https://example.com/welcome.jpg')])

# Command to deploy
def deploy(update: Update, context: CallbackContext) -> None:
    # In a real scenario, you would include deployment logic here.
    update.message.reply_text("Please provide your GitHub repository link.")
    # Collect repository info and deploy your bot

# Error handling
def error(update: Update, context: CallbackContext) -> None:
    logger.warning(f"Update {update} caused error {context.error}")

def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("deploy", deploy))

    # Log all errors
    dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop it
    updater.idle()

if __name__ == '__main__':
    main()
