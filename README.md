# Telegram Music Bot

This bot helps you deploy and host a music bot directly from your GitHub repository.

## Features

- Deploys music bot from GitHub.
- Sends a welcome message with an image.
- Handles errors and deployment logs.

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`
- Docker (optional)

## How to Deploy

1. Clone the repository.
2. Create a `.env` file and add your `TELEGRAM_BOT_TOKEN`.
3. Run the bot:
    - `python bot.py`
    - Or use Docker: `docker build -t music-bot . && docker run music-bot`
