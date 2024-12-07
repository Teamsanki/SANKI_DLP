import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from telegram import InputMediaPhoto

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Your Bot Token (directly placed here for simplicity)
TOKEN = "7908847221:AAFo2YqgQ4jYG_Glbp96sINg79zF8T6EWoo"

# Start command
async def start(update: Update, context: CallbackContext) -> None:
    welcome_msg = "Welcome to the Music Bot! This bot will help you deploy and host your bot on GitHub."
    await update.message.reply_text(welcome_msg)
    # Send a welcome image
    await update.message.reply_media_group([InputMediaPhoto('https://example.com/welcome.jpg')])

# Command to deploy
async def deploy(update: Update, context: CallbackContext) -> None:
    # In a real scenario, you would include deployment logic here.
    await update.message.reply_text("Please provide your GitHub repository link.")
    # Collect repository info and deploy your bot

# Error handling
def error(update: Update, context: CallbackContext) -> None:
    logger.warning(f"Update {update} caused error {context.error}")

async def main() -> None:
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("deploy", deploy))

    # Log all errors
    application.add_error_handler(error)

    # Start the Bot
    await application.run_polling()

if __name__ == '__main__':
    # Directly call the polling method without asyncio.run
    main()
