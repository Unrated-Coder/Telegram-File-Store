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
from helper_func import get_next_image
from database.database import *

BAN_SUPPORT = f"{BAN_SUPPORT}"

@Bot.on_message(filters.command('start') & filters.private)
async def start_command(client: Client, message: Message):
    user_id = message.from_user.id

    banned_users = await db.get_ban_users()
    if user_id in banned_users:
        return await message.reply_text(
            "<b>⛔️ You are Bᴀɴɴᴇᴅ from using this bot.</b>\n\n"
            "<i>Contact support if you think this is a mistake.</i>",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Contact Support", url=BAN_SUPPORT, style="success")]]
            )
        )
    if not await is_subscribed(client, user_id):
        return await not_joined(client, message)

    FILE_AUTO_DELETE = await db.get_del_timer()

    if not await db.present_user(user_id):
        try:
            await db.add_user(user_id)
        except:
            pass

    text = message.text
    if len(text) > 7:
        try:
            base64_string = text.split(" ", 1)[1]
        except IndexError:
            return

        string = await decode(base64_string)
        argument = string.split("-")

        ids = []
        if not hasattr(client, "db_channel") or not client.db_channel:
            return await message.reply_text("<b>Eʀʀᴏʀ:</b> Dᴀᴛᴀʙᴀsᴇ Cʜᴀɴɴᴇʟ ɴᴏᴛ ᴄᴏɴғɪɢᴜʀᴇᴅ ᴘʀᴏᴘᴇʀʟʏ!")

        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
                ids = range(start, end + 1) if start <= end else list(range(start, end - 1, -1))
            except Exception as e:
                print(f"Error decoding IDs: {e}")
                return

        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except Exception as e:
                print(f"Error decoding ID: {e}")
                return

        temp_msg = await message.reply("<b>⏳ ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ ᴀ ꜱᴇᴄᴏɴᴅ... ɪ'ᴍ ᴡᴏʀᴋɪɴɢ ᴍʏ ᴍᴀɢɪᴄ ꜰᴏʀ ʏᴏᴜ! ✨</b>")
        try:
            messages = await get_messages(client, ids)
        except Exception as e:
            await message.reply_text("<b>ᴏʜ, ꜱᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ! ᴅᴏɴ'ᴛ ʙʟᴀᴍᴇ ᴍᴇ, ʏᴏᴜ ᴄʟᴜᴍꜱʏ ʜᴜᴍᴀɴ! 🙄</b>")
            print(f"Error getting messages: {e}")
            return
        finally:
            await temp_msg.delete()
 
        from copy_engine import copy_video
        codeflix_msgs = []

        for msg in messages:
            original_caption = msg.caption.html if msg.caption else ""
            caption = f"{original_caption}\n\n{CUSTOM_CAPTION}" if CUSTOM_CAPTION else original_caption
            reply_markup = msg.reply_markup if DISABLE_CHANNEL_BUTTON else None

            try:
                if msg.video:
                    snt_msg = await copy_video(
                        pyrogram_bot=client,
                        chat_id=message.from_user.id,
                        from_chat_id=client.db_channel.id,
                        message_id=msg.id,
                        caption=caption,
                        reply_markup=reply_markup,
                        protect_content=PROTECT_CONTENT
                    )
                else:
                    snt_msg = await msg.copy(
                        chat_id=message.from_user.id,
                        caption=caption,
                        parse_mode=ParseMode.HTML,
                        reply_markup=reply_markup,
                        protect_content=PROTECT_CONTENT
                    )
                await asyncio.sleep(0.5)
                codeflix_msgs.append(snt_msg)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                if msg.video:
                    copied_msg = await copy_video(
                        pyrogram_bot=client,
                        chat_id=message.from_user.id,
                        from_chat_id=client.db_channel.id,
                        message_id=msg.id,
                        caption=caption,
                        reply_markup=reply_markup,
                        protect_content=PROTECT_CONTENT
                    )
                else:
                    copied_msg = await msg.copy(
                        chat_id=message.from_user.id,
                        caption=caption,
                        parse_mode=ParseMode.HTML,
                        reply_markup=reply_markup,
                        protect_content=PROTECT_CONTENT
                    )
                codeflix_msgs.append(copied_msg)
            except Exception as e:
                print(e)
                pass

        if FILE_AUTO_DELETE > 0:
            notification_msg = await message.reply(
                f"<b>ʜᴍᴘʜ! ᴛʜɪꜱ ꜰɪʟᴇ ᴡɪʟʟ ᴠᴀɴɪꜱʜ ɪɴ  {get_exp_time(FILE_AUTO_DELETE)}. ꜱᴀᴠᴇ ɪᴛ ᴏʀ ꜰᴏʀᴡᴀʀᴅ ɪᴛ, ʏᴏᴜ ᴄʟᴜᴍꜱʏ ʜᴜᴍᴀɴ, ʙᴇꜰᴏʀᴇ ɪ ᴅᴇꜱᴛʀᴏʏ ɪᴛ! 💥</b>"
            )

            await asyncio.sleep(FILE_AUTO_DELETE)

            for snt_msg in codeflix_msgs:    
                if snt_msg:
                    try:    
                        await snt_msg.delete()  
                    except Exception as e:
                        print(f"Error deleting message {snt_msg.id}: {e}")

            try:
                retrieve_active = await db.get_retrieve_status()
                if retrieve_active:
                    reload_url = (
                        f"https://t.me/{client.username}?start={message.command[1]}"
                        if message.command and len(message.command) > 1
                        else None
                    )
                    keyboard = InlineKeyboardMarkup(
                        [[InlineKeyboardButton("ɢᴇᴛ ꜰɪʟᴇ ᴀɢᴀɪɴ!", url=reload_url, style="success")]]
                    ) if reload_url else None

                    await notification_msg.edit(
                        CUSTOM_DELETE_ALERT,
                        reply_markup=keyboard
                    )
                else:
                    await notification_msg.delete()
            except Exception as e:
                print(f"Error updating or deleting notification message: {e}")
    else:
        reply_markup = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('ᴀɴɪᴍᴇꜱ', url='https://t.me/UNRATED_CODER', style="primary"),
                InlineKeyboardButton('ʙᴀꜱᴇ', url='https://t.me/UNRATED_CODER', style="primary")],
                [InlineKeyboardButton('• ᴀʙᴏᴜᴛ', callback_data='about', style="primary"),
                InlineKeyboardButton(' ʜᴇʟᴘ •', callback_data='help', style="primary")],
                [InlineKeyboardButton("ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url='https://t.me/UNRATED_CODER', style="success")]
            ]
        )
        caption = START_MSG
        if "{first}" in caption: caption = caption.replace("{first}", message.from_user.first_name or "")
        if "{last}" in caption: caption = caption.replace("{last}", message.from_user.last_name or "")
        if "{username}" in caption: caption = caption.replace("{username}", "" if not message.from_user.username else '@' + message.from_user.username)
        if "{mention}" in caption: caption = caption.replace("{mention}", message.from_user.mention or "")
        if "{id}" in caption: caption = caption.replace("{id}", str(message.from_user.id))

        await message.reply_photo(
            photo=get_next_image(message.chat.id),
            caption=caption,
            reply_markup=reply_markup,
            has_spoiler=True,
            message_effect_id=5104841245755180586)
        
        return



# =====================================================================================##
#                         ✨ MADE BY UNRATED CODER ✨
#                  Join Updates Channel: https://t.me/UNRATED_CODER
#====================================================================================##



chat_data_cache = {}

async def not_joined(client: Client, message: Message):
    temp = await message.reply("<b><i>ᴡᴀɪᴛ ᴀ ꜱᴇᴄ, ʏᴏᴜ ɪᴍᴘᴀᴛɪᴇɴᴛ ᴍᴏʀᴛᴀʟ... ᴏʀ ᴀʀᴇ ʏᴏᴜ ᴊᴜꜱᴛ ᴇxᴄɪᴛᴇᴅ ᴛᴏ ꜱᴇᴇ ᴍᴇ? 😏</i></b>")

    user_id = message.from_user.id
    buttons = []
    count = 0

    try:
        all_channels = await db.show_channels()
        for total, chat_id in enumerate(all_channels, start=1):
            mode = await db.get_channel_mode(chat_id)

            await message.reply_chat_action(ChatAction.TYPING)

            if not await is_sub(client, user_id, chat_id):
                try:
                    if chat_id in chat_data_cache:
                        data = chat_data_cache[chat_id]
                    else:
                        data = await client.get_chat(chat_id)
                        chat_data_cache[chat_id] = data

                    name = data.title

                    if mode == "on" and not data.username:
                        invite = await client.create_chat_invite_link(
                            chat_id=chat_id,
                            creates_join_request=True,
                            expire_date=datetime.utcnow() + timedelta(seconds=FSUB_LINK_EXPIRY) if FSUB_LINK_EXPIRY else None
                            )
                        link = invite.invite_link

                    else:
                        if data.username:
                            link = f"https://t.me/{data.username}"
                        else:
                            invite = await client.create_chat_invite_link(
                                chat_id=chat_id,
                                expire_date=datetime.utcnow() + timedelta(seconds=FSUB_LINK_EXPIRY) if FSUB_LINK_EXPIRY else None)
                            link = invite.invite_link

                    buttons.append([InlineKeyboardButton(text=f"{name}", url=link, style="primary")])
                    count += 1
                    await temp.edit(f"<b>{'! ' * count}</b>")

                except Exception as e:
                    print(f"Error with chat {chat_id}: {e}")
                    return await temp.edit(
                        f"<b><i>! Eʀʀᴏʀ, Cᴏɴᴛᴀᴄᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ ᴛᴏ sᴏʟᴠᴇ ᴛʜᴇ ɪssᴜᴇs @UNRATED_CODER</i></b>\n"
                        f"<blockquote expandable><b>Rᴇᴀsᴏɴ:</b> {e}</blockquote>"
                    )

        try:
            buttons.append([
                InlineKeyboardButton(
                    text='♻️ ᴛʀʏ ᴀɢᴀɪɴ',
                    url=f"https://t.me/{client.username}?start={message.command[1]}",
                    style="success"
                )
            ])
        except IndexError:
            pass

        caption = FORCE_MSG
        if "{first}" in caption: caption = caption.replace("{first}", message.from_user.first_name or "")
        if "{last}" in caption: caption = caption.replace("{last}", message.from_user.last_name or "")
        if "{username}" in caption: caption = caption.replace("{username}", "" if not message.from_user.username else '@' + message.from_user.username)
        if "{mention}" in caption: caption = caption.replace("{mention}", message.from_user.mention or "")
        if "{id}" in caption: caption = caption.replace("{id}", str(message.from_user.id))

        await message.reply_photo(
            photo=get_next_image(message.chat.id),
            caption=caption,
            reply_markup=InlineKeyboardMarkup(buttons),
            has_spoiler=True
        )

    except Exception as e:
        print(f"Final Error: {e}")
        await temp.edit(
            f"<b><i>! Eʀʀᴏʀ, Cᴏɴᴛᴀᴄᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ ᴛᴏ sᴏʟᴠᴇ ᴛʜᴇ ɪssᴜᴇs @UNRATED_CODER</i></b>\n"
            f"<blockquote expandable><b>Rᴇᴀsᴏɴ:</b> {e}</blockquote>"
        )


@Bot.on_message(filters.command('commands') & filters.private & admin)
async def bcmd(bot: Bot, message: Message):        
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data = "close", style="danger")]])
    await message.reply(text=CMD_TXT, reply_markup = reply_markup, quote= True)
