# =====================================================================================##
#
#  ██╗░░██╗███╗░░██╗██████╗░░█████╗░████████╗███████╗██████╗░
#  ██║░░██║████╗░██║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
#  ██║░░██║██╔██╗██║██████╔╝███████║░░░██║░░░█████╗░░██║░░██║
#  ██║░░██║██║╚████║██╔══██╗██╔══██║░░░██║░░░██╔══╝░░██║░░██║
#  ╚██████╔╝██║░╚███║██║░░██║██║░░██║░░░██║░░░███████╗██████╔╝
#  ░╚═════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░
#
#  ░██████╗░██████╗░██████╗░███████╗██████╗░
#  ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
#  ██║░░░░░██║░░░██║██║░░██║█████╗░░██████╔╝
#  ██║░░░░░██║░░░██║██║░░██║██╔══╝░░██╔══██╗
#  ╚██████╗╚██████╔╝██████╔╝███████╗██║░░██║
#  ░╚═════╝░╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝
#
#                         ✨ MADE BY UNRATED CODER ✨
#                  Join Updates Channel: https://t.me/UNRATED_CODER
#=====================================================================================##

import asyncio
import pyromod.listen
import inspect
from pyrogram.handlers import MessageHandler

# Monkeypatch pyromod's MessageHandler.check to safely handle both synchronous and asynchronous custom/standard filters.
async def safe_check(self, client, update):
    listener = client.listening.get(update.chat.id)
    if listener and not listener['future'].done():
        if callable(listener['filters']):
            res = listener['filters'](client, update)
            if inspect.isawaitable(res):
                return await res
            return res
        return True
    if callable(self.filters):
        res = self.filters(client, update)
        if inspect.isawaitable(res):
            return await res
        return res
    return True

MessageHandler.check = safe_check

from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime
from config import *


name ="""
 BY UNRATED CODER
"""


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        if CHANNEL_ID:
            try:
                db_channel = await self.get_chat(CHANNEL_ID)
                self.db_channel = db_channel
                test = await self.send_message(chat_id = db_channel.id, text = "Test Message")
                await test.delete()
            except Exception as e:
                self.LOGGER(__name__).warning(e)
                self.LOGGER(__name__).warning(f"Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}")
                self.LOGGER(__name__).info("\nBot failed to initialize correctly. Join https://t.me/UNRATED_CODER for support")
        else:
            self.LOGGER(__name__).warning("CHANNEL_ID is not set. Bot will not be able to store/retrieve files.")

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot Running..!\n\nCreated by \n@UNRATED_CODER")
        self.LOGGER(__name__).info(f"""BOT DEPLOYED BY @UNRATED_CODER""")

        self.set_parse_mode(ParseMode.HTML)
        self.username = usr_bot_me.username
        self.LOGGER(__name__).info(f"Bot Running..! Made by @UNRATED_CODER")


        try:
            from pyrogram.types import BotCommand
            await self.set_bot_commands([
                BotCommand("start", "sᴛᴀʀᴛs ᴏʀ ʀᴇsᴛᴀʀᴛs ᴛʜᴇ ʙᴏᴛ"),
                BotCommand("help", "sʜᴏᴡs ᴛʜᴇ sᴜᴘᴘᴏʀᴛ/ʜᴇʟᴘ ᴍᴇssᴀɢᴇ"),
                BotCommand("commands", "ʟɪsᴛs ᴀʟʟ ᴀᴠᴀɪʟᴀʙʟᴇ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs"),
                BotCommand("stats", "sʜᴏᴡs ʙᴏᴛ sᴛᴀᴛɪsᴛɪᴄs"),
                BotCommand("ping", "ᴄʜᴇᴄᴋs ᴛʜᴇ ʙᴏᴛ's ᴘɪɴɢ ʟᴀᴛᴇɴᴄʏ"),
                BotCommand("users", "sʜᴏᴡs ᴛʜᴇ ᴛᴏᴛᴀʟ ᴜsᴇʀ ᴄᴏᴜɴᴛ"),
                BotCommand("add_admin", "ᴀᴅᴅs ᴀ ɴᴇᴡ ᴀᴅᴍɪɴ ᴜsᴇʀ"),
                BotCommand("admins", "ʟɪsᴛs ᴀʟʟ ᴀᴄᴛɪᴠᴇ ᴀᴅᴍɪɴ ɪᴅs"),
                BotCommand("deladmin", "ʀᴇᴍᴏᴠᴇs ᴀɴ ᴀᴅᴍɪɴ ᴜsᴇʀ"),
                BotCommand("addchnl", "ᴀᴅᴅs ᴀ ɴᴇᴡ ғᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ"),
                BotCommand("delchnl", "ʀᴇᴍᴏᴠᴇs ᴀ ғᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ"),
                BotCommand("listchnl", "sʜᴏᴡs ᴛʜᴇ ғᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟs"),
                BotCommand("fsub_mode", "ᴛᴏɢɢʟᴇs ғᴏʀᴄᴇ sᴜʙsᴄʀɪᴘᴛɪᴏɴ ᴍᴏᴅᴇ"),
                BotCommand("ban", "ʙᴀɴs ᴀ ᴜsᴇʀ ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ"),
                BotCommand("unban", "ᴜɴʙᴀɴs ᴀ ᴜsᴇʀ"),
                BotCommand("banlist", "sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ ʙᴀɴɴᴇᴅ ᴜsᴇʀs"),
                BotCommand("batch", "ᴄʀᴇᴀᴛᴇs ᴀ ʙᴀᴛᴄʜ ᴏғ ғɪʟᴇ ʟɪɴᴋs"),
                BotCommand("custom_batch", "sᴀᴠᴇs ᴄᴜsᴛᴏᴍ ᴍᴇssᴀɢᴇs ᴀs ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ"),
                BotCommand("genlink", "ɢᴇɴᴇʀᴀᴛᴇs ᴀ sɪɴɢʟᴇ sʜᴀʀᴇ ʟɪɴᴋ"),
                BotCommand("broadcast", "sᴇɴᴅs ᴀ ʙʀᴏᴀᴅᴄᴀsᴛ ᴍᴇssᴀɢᴇ"),
                BotCommand("pbroadcast", "sᴇɴᴅs ᴀ ᴘʜᴏᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ"),
                BotCommand("dbroadcast", "sᴇɴᴅs ᴀ sɪʟᴇɴᴛ ʙʀᴏᴀᴅᴄᴀsᴛ"),
                BotCommand("dlt_time", "sᴇᴛs ᴛʜᴇ ᴀᴜᴛᴏ-ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇr"),
                BotCommand("check_dlt_time", "ᴄʜᴇᴄᴋs ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴀᴜᴛᴏ-ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇʀ"),
                BotCommand("retrieve_on", "ᴇɴᴀʙʟᴇs ᴛʜᴇ ᴅᴇʟᴇᴛɪᴏɴ ᴀʟᴇʀᴛ ᴍᴇssᴀɢᴇ"),
                BotCommand("retrieve_off", "ᴅɪsᴀʙʟᴇs ᴛʜᴇ ᴅᴇʟᴇᴛɪᴏɴ ᴀʟᴇʀᴛ ᴍᴇssᴀɢᴇ")
            ])
            self.LOGGER(__name__).info("Bot commands set successfully starting with start.")
        except Exception as e:
            self.LOGGER(__name__).warning(f"Error setting bot commands: {e}")

        try: await self.send_message(OWNER_ID, text = f"<b><blockquote> Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ by @UNRATED_CODER</blockquote></b>")
        except: pass

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")

    def run(self):
        """Run the bot."""
        super().run()

# =====================================================================================##
#                         ✨ MADE BY UNRATED CODER ✨
#                  Join Updates Channel: https://t.me/UNRATED_CODER
#====================================================================================##
