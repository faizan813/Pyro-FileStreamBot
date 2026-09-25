import logging
import asyncio
from aiohttp import web
from pyrogram import Client
from WebStreamer.vars import Var
from WebStreamer.bot import StreamBot
from WebStreamer.server import web_server
import pyrogram.session.session

# Force the library to skip heavy client clock validation and sync with Telegram
pyrogram.session.session.Session.START_TIMEOUT = 60

async def main():
    # Start the web server correctly using aiohttp web components
    app = await web_server()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, Var.BIND_ADDRESS, Var.PORT)
    await site.start()
    logging.info(f"Server started on {Var.BIND_ADDRESS}:{Var.PORT}")
    
    # Start the Telegram Bot Client safely
    await StreamBot.start()
    logging.info("Bot started successfully.")
    
    # Keep the service running
    await asyncio.Event().wait()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
