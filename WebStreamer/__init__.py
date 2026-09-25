import logging
from pyrogram import Client
from WebStreamer.vars import Var
import pyrogram.session.session

# Force the library to skip heavy client clock validation and sync with Telegram
pyrogram.session.session.Session.START_TIMEOUT = 60

StreamBot = Client(
    session_name="WebStreamer",
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    bot_token=Var.BOT_TOKEN,
    sleep_threshold=Var.SLEEP_THRESHOLD,
    workers=Var.WORKERS
)
