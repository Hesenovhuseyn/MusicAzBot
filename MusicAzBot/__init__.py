# @MusicAzBot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə


import logging
from pyrogram import Client
from MusicAzBot.config import Config

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)

MusicAzBot = Client(
    'MusicAzBot',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)
