# Savvy Music Bot

Savvy Music Bot is a powerful Telegram bot for managing and streaming music in your Telegram groups and channels.

## Features

- Stream music from various sources.
- Manage music playback in groups.
- User-friendly commands.
- More features...
## Deploying on koyeb
[![Deploy to Koyeb](https://www.koyeb.com/deploy.svg)](https://www.koyeb.com/deploy?repository=https://github.com/Noob-savvy/SavvyMusic_v1)

## Deploying on Heroku

You can easily deploy Savvy Music on Heroku using the following steps:

1. Click on the "Deploy to Heroku" button below.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new-app?template=https://github.com/Noob-savvy/SavvyMusic_v1)

2. Fill in the required environment variables during the deployment process.
3. Click "Deploy" and wait for the deployment to complete.
4. Once deployed, open your app on Heroku and go to the "Resources" tab.
5. Enable the worker by turning the switch on.
6. Your Savvy Music Bot is now up and running on Heroku!
# manually deployment 
## Clone the repository
git clone https://github.com/Noob-savvy/SavvyMusic_v1.git

## Change into the project directory
cd SavvyMusic

## Install dependencies
pip install -r requirements.txt

## Set up your configuration by copying the example cp config.py.example config.py

## Edit config.py with your own values using a text editor
## For example, using nano:
nano config.py

## Run the bot
python -m SavvyMusic
