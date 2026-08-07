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
import os
import random
import sys
import time
from datetime import datetime, timedelta
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode, ChatAction
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup, ChatInviteLink, ChatPrivileges
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated, UserNotParticipant
from bot import Bot
from config import *
from helper_func import *
from database.database import *
from plugins.Unrated_Coder import check_owner_only, check_admin_or_owner


@Bot.on_message(filters.command('stats'))
async def stats(bot: Bot, message: Message):
    if not await check_admin_or_owner(message):
        return

    uptime = getattr(bot, "uptime", None)
    if not uptime:
        bot.uptime = datetime.now()
        uptime = bot.uptime
    now = datetime.now()
    delta = now - uptime
    uptime_str = get_readable_time(int(delta.total_seconds()))
    if not uptime_str:
        uptime_str = "0s"

    import psutil
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent

    users = await db.full_userbase()
    users_count = len(users)

    await message.reply(BOT_STATS_TEXT.format(
        uptime=uptime_str,
        cpu=cpu,
        ram=ram,
        users=users_count
    ))



WAIT_MSG = "<b>⏳ ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ ᴀ ꜱᴇᴄᴏɴᴅ... ɪ'ᴍ ᴡᴏʀᴋɪɴɢ ᴍʏ ᴍᴀɢɪᴄ ꜰᴏʀ ʏᴏᴜ! ✨</b>"



@Bot.on_message(filters.command('users') & filters.private)
async def get_users(client: Bot, message: Message):
    if not await check_admin_or_owner(message):
        return
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    users = await db.full_userbase()
    await msg.edit(f"{len(users)} users are using this bot")





@Bot.on_message(filters.private & filters.command('dlt_time'))
async def set_delete_time(client: Bot, message: Message):
    if not await check_admin_or_owner(message):
        return
    try:
        duration = int(message.command[1])

        await db.set_del_timer(duration)

        await message.reply(f"<b>Dᴇʟᴇᴛᴇ Tɪᴍᴇʀ ʜᴀs ʙᴇᴇɴ sᴇᴛ ᴛᴏ <blockquote>{duration} sᴇᴄᴏɴᴅs.</blockquote></b>")

    except (IndexError, ValueError):
        await message.reply("<b>Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴠᴀʟɪᴅ ᴅᴜʀᴀᴛɪᴏɴ ɪɴ sᴇᴄᴏɴᴅs.</b> Usage: /dlt_time {duration}")

@Bot.on_message(filters.private & filters.command('check_dlt_time'))
async def check_delete_time(client: Bot, message: Message):
    if not await check_admin_or_owner(message):
        return
    duration = await db.get_del_timer()

    await message.reply(f"<b><blockquote>Cᴜʀʀᴇɴᴛ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇʀ ɪs sᴇᴛ ᴛᴏ {duration}sᴇᴄᴏɴᴅs.</blockquote></b>")


@Bot.on_message(filters.private & filters.command('retrieve_on'))
async def retrieve_on_command(client: Bot, message: Message):
    if not await check_admin_or_owner(message):
        return
    await db.set_retrieve_status(True)
    await message.reply("<b><blockquote>Rᴇᴛʀɪᴇᴠᴇ Oɴ! Dᴇʟᴇᴛɪᴏɴ ᴀʟᴇʀᴛ ᴍᴇssᴀɢᴇ ᴡɪʟʟ ʙᴇ sʜᴏᴡɴ ᴀɴᴅ 'ɢᴇᴛ ғɪʟᴇ ᴀɢᴀɪɴ' ʙᴜᴛᴛᴏɴ ᴡɪʟʟ ʙᴇ ᴀᴄᴛɪᴠᴇ. ✅</blockquote></b>")


@Bot.on_message(filters.private & filters.command('retrieve_off'))
async def retrieve_off_command(client: Bot, message: Message):
    if not await check_admin_or_owner(message):
        return
    await db.set_retrieve_status(False)
    await message.reply("<b><blockquote>Rᴇᴛʀɪᴇᴠᴇ Oғғ! Dᴇʟᴇᴛɪᴏɴ ᴀʟᴇʀᴛ ᴍᴇssᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ ᴇɴᴛɪʀᴇʟʏ ᴀғᴛᴇʀ ғɪʟᴇs ᴀʀᴇ ᴠᴀɴɪsʜᴇᴅ. ❌</blockquote></b>")


@Bot.on_message(filters.command('ping'))
async def ping(bot: Bot, message: Message):
    start_time = time.time()
    reply = await message.reply("<b>Pɪɴɢɪɴɢ...</b>")
    end_time = time.time()
    latency = (end_time - start_time) * 1000
    await reply.edit(f"<b>Pᴏɴɢ! 🏓 <blockquote>{latency:.2f}ms</blockquote></b>")

# =====================================================================================##
#                         ✨ MADE BY UNRATED CODER ✨
#                  Join Updates Channel: https://t.me/UNRATED_CODER
#====================================================================================##
