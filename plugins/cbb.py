from pyrogram import Client, filters
from bot import Bot
from config import *
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.database import *
from helper_func import get_next_image

from pyrogram.types import InputMediaPhoto

@Bot.on_callback_query(filters.regex("^(help|about|start|close|rfs_ch_|rfs_toggle_|fsub_back)"))
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data

    if data == "help":
        await query.answer()
        caption = HELP_TXT.replace("{first}", query.from_user.first_name or "") if "{first}" in HELP_TXT else HELP_TXT

        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start', style="primary"),
             InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data='close', style="danger")]
        ])

        if query.message.photo or query.message.document or query.message.video or query.message.animation:
            await query.message.edit_media(
                media=InputMediaPhoto(
                    media=get_next_image(query.message.chat.id),
                    caption=caption,
                    has_spoiler=True
                ),
                reply_markup=reply_markup
            )
        else:
            await query.message.edit_text(
                text=caption,
                disable_web_page_preview=True,
                reply_markup=reply_markup
            )

    elif data == "about":
        await query.answer()
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start', style="primary"),
             InlineKeyboardButton('ᴄʟᴏꜱᴇ', callback_data='close', style="danger")]
        ])

        if query.message.photo or query.message.document or query.message.video or query.message.animation:
            await query.message.edit_media(
                media=InputMediaPhoto(
                    media=get_next_image(query.message.chat.id),
                    caption=ABOUT_TXT.replace("{first}", query.from_user.first_name),
                    has_spoiler=True
                ),
                reply_markup=reply_markup
            )
        else:
            await query.message.edit_text(
                text=ABOUT_TXT.replace("{first}", query.from_user.first_name),
                disable_web_page_preview=True,
                reply_markup=reply_markup
            )

    elif data == "start":
        await query.answer()
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton('ᴀɴɪᴍᴇꜱ', url='https://t.me/UNRATED_CODER', style="primary"),
             InlineKeyboardButton('ʙᴀꜱᴇ', url='https://t.me/UNRATED_CODER', style="primary")],
            [InlineKeyboardButton('• ᴀʙᴏᴜᴛ', callback_data='about', style="primary"),
             InlineKeyboardButton(' ʜᴇʟᴘ •', callback_data='help', style="primary")],
            [InlineKeyboardButton("ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url='https://t.me/UNRATED_CODER', style="success")]
        ])

        if query.message.photo or query.message.document or query.message.video or query.message.animation:
            caption = START_MSG
            if "{first}" in caption: caption = caption.replace("{first}", query.from_user.first_name or "")
            if "{last}" in caption: caption = caption.replace("{last}", query.from_user.last_name or "")
            if "{username}" in caption: caption = caption.replace("{username}", "" if not query.from_user.username else '@' + query.from_user.username)
            if "{mention}" in caption: caption = caption.replace("{mention}", query.from_user.mention or "")
            if "{id}" in caption: caption = caption.replace("{id}", str(query.from_user.id))

            await query.message.edit_media(
                media=InputMediaPhoto(
                    media=get_next_image(query.message.chat.id),
                    caption=caption,
                    has_spoiler=True
                ),
                reply_markup=reply_markup
            )
        else:
            text = START_MSG
            if "{first}" in text: text = text.replace("{first}", query.from_user.first_name or "")
            if "{last}" in text: text = text.replace("{last}", query.from_user.last_name or "")
            if "{username}" in text: text = text.replace("{username}", "" if not query.from_user.username else '@' + query.from_user.username)
            if "{mention}" in text: text = text.replace("{mention}", query.from_user.mention or "")
            if "{id}" in text: text = text.replace("{id}", str(query.from_user.id))

            await query.message.edit_text(
                text=text,
                disable_web_page_preview=True,
                reply_markup=reply_markup
            )

    elif data == "close":
        await query.answer()
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

    elif data.startswith("rfs_ch_"):
        await query.answer()
        cid = int(data.split("_")[2])
        try:
            chat = await client.get_chat(cid)
            mode = await db.get_channel_mode(cid)
            status = "🟢 ᴏɴ" if mode == "on" else "🔴 ᴏғғ"
            new_mode = "ᴏғғ" if mode == "on" else "on"
            buttons = [
                [InlineKeyboardButton(f"ʀᴇǫ ᴍᴏᴅᴇ {'OFF' if mode == 'on' else 'ON'}", callback_data=f"rfs_toggle_{cid}_{new_mode}", style="danger" if mode == 'on' else "success")],
                [InlineKeyboardButton("‹ ʙᴀᴄᴋ", callback_data="fsub_back", style="primary")]
            ]
            await query.message.edit_text(
                f"Channel: {chat.title}\nCurrent Force-Sub Mode: {status}",
                reply_markup=InlineKeyboardMarkup(buttons)
            )
        except Exception:
            await query.answer("Failed to fetch channel info", show_alert=True)

    elif data.startswith("rfs_toggle_"):
        cid, action = data.split("_")[2:]
        cid = int(cid)
        mode = "on" if action == "on" else "off"

        await db.set_channel_mode(cid, mode)
        await query.answer(f"Force-Sub set to {'ON' if mode == 'on' else 'OFF'}")

        chat = await client.get_chat(cid)
        status = "🟢 ON" if mode == "on" else "🔴 OFF"
        new_mode = "off" if mode == "on" else "on"
        buttons = [
            [InlineKeyboardButton(f"ʀᴇǫ ᴍᴏᴅᴇ {'OFF' if mode == 'on' else 'ON'}", callback_data=f"rfs_toggle_{cid}_{new_mode}", style="danger" if mode == 'on' else "success")],
            [InlineKeyboardButton("‹ ʙᴀᴄᴋ", callback_data="fsub_back", style="primary")]
        ]
        await query.message.edit_text(
            f"Channel: {chat.title}\nCurrent Force-Sub Mode: {status}",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif data == "fsub_back":
        await query.answer()
        channels = await db.show_channels()
        buttons = []
        for cid in channels:
            try:
                chat = await client.get_chat(cid)
                mode = await db.get_channel_mode(cid)
                status = "🟢" if mode == "on" else "🔴"
                buttons.append([InlineKeyboardButton(f"{status} {chat.title}", callback_data=f"rfs_ch_{cid}", style="primary")])
            except:
                continue

        await query.message.edit_text(
            "sᴇʟᴇᴄᴛ ᴀ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴛᴏɢɢʟᴇ ɪᴛs ғᴏʀᴄᴇ-sᴜʙ ᴍᴏᴅᴇ:",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
