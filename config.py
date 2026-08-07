import os
from os import environ, getenv
import logging
from dotenv import load_dotenv

load_dotenv()
from logging.handlers import RotatingFileHandler

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", "0"))
API_HASH = os.environ.get("API_HASH", "")

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "0"))
OWNER = os.environ.get("OWNER", "")
OWNER_ID = int(os.environ.get("OWNER_ID", "0"))
PORT = os.environ.get("PORT", "8001")
DB_URI = os.environ.get("DATABASE_URL", "")

if not TG_BOT_TOKEN:
    logging.warning("TG_BOT_TOKEN is not set!")
if APP_ID == 0:
    logging.warning("APP_ID is not set!")
if not API_HASH:
    logging.warning("API_HASH is not set!")
if not DB_URI:
    logging.warning("DATABASE_URL is not set!")
DB_NAME = os.environ.get("DB_NAME", "Filestore")
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "10"))
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/AniReal_Chat_Group_Asia")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/0591ce5558c3ec8fe7612-263292508134daf3e1.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/fdc4357abfaba23255e98-24d1bbfa3888cdfcfe.jpg")

HELP_TXT = "<b>ʜᴜʜʜʜʜʜ!... ʜᴇʟᴘ? 😮‍💨</b>\n<b><blockquote>⚡ ᴛʜɪs ᴘʀɪᴠᴀᴛᴇ ᴘʀᴇᴍɪᴜᴍ ʙᴏᴛ ɪs ᴍʏ ᴘᴇʀsᴏɴᴀʟ ɢᴀʀᴅᴇɴ! ᴏɴʟʏ ᴍʏ ᴄʜᴏsᴇɴ ᴀᴅᴍɪɴs & ᴍʏ ᴅᴀʀʟɪɴɢs ᴄᴀɴ ᴛᴏᴜᴄʜ ɪᴛ. 🔐 ᴛᴏ sᴛᴇᴀʟ ᴀ ɢʟɪᴍᴘsᴇ ᴀɴᴅ ɢᴇᴛ ꜰɪʟᴇs, ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴀsᴋ ꜰᴏʀ ᴛʜᴇ ᴅɪʀᴇᴄᴛ ʟɪɴᴋ! 🎯 ᴛʜɪs ɪs ᴇxᴄʟᴜsɪᴠᴇʟʏ ꜰᴏʀ ʏᴏᴜ. ɢᴇᴛ ʏᴏᴜʀ ꜰɪʟᴇs sᴇᴄᴜʀᴇʟʏ, ᴀɴᴅ ᴅᴏɴ'ᴛ ᴍᴀᴋᴇ ᴍᴇ ᴡᴀɪᴛ!</blockquote></b>\n<b>• ᴊᴏɪɴ ᴍʏ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ: @Unrated_Coder\nᴡᴀɴᴛ ᴍᴏʀᴇ ᴏꜰ ᴍᴇ? ᴜsᴇ /help!</b>"

ABOUT_TXT = """<b>🤖 ɪꜱʜᴛᴀʀ ʙᴏᴛ - ᴀʙᴏᴜᴛ ᴍᴇ</b>
<b><blockquote>💡 ᴍʏ ꜱᴛᴀᴛᴜꜱ: <code>ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀɪᴛɪɴɢ 24/7</code>
🚀 ᴘᴏᴡᴇʀꜱ: ɪɴꜱᴛᴀɴᴛ ᴀɴɪᴍᴇ & ꜱᴇᴄʀᴇᴛ ꜰɪʟᴇꜱ.
🔗 ᴀᴄᴄᴇꜱꜱ: ɢᴇᴛ ᴛʜᴇᴍ ᴅɪʀᴇᴄᴛʟʏ ᴛʜʀᴏᴜɢʜ ᴍʏ ꜱᴘᴇᴄɪᴀʟ ʟɪɴᴋꜱ.
⚡ ᴜᴘᴛɪᴍᴇ: ᴀʟᴡᴀʏꜱ ᴀᴄᴛɪᴠᴇ ᴊᴜꜱᴛ ꜰᴏʀ ʏᴏᴜ.
🌐 ᴄʜᴀɴɴᴇʟꜱ: ᴊᴏɪɴ ᴜꜱ, ᴅᴏɴ'ᴛ ʙᴇ ꜱʜʏ!</blockquote></b>
<b><blockquote>◈ ᴄʀᴇᴀᴛᴏʀ: <a href="https://t.me/UNRATED_CODER">ᴜɴʀᴀᴛᴇᴅ ᴄᴏᴅᴇʀ</a>\n◈ ꜰᴏᴜɴᴅᴇʀ: <a href="https://t.me/UNRATED_CODER">ᴜɴʀᴀᴛᴇᴅ ᴄᴏᴅᴇʀ</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href="https://t.me/UNRATED_CODER">ᴜɴʀᴀᴛᴇᴅ ᴄᴏᴅᴇʀ</a></blockquote></b>"""
START_MSG = os.environ.get("START_MESSAGE", "<b>💖 ʜᴇʟʟᴏ {first}! 🥀\n<blockquote expandable>ɪ'ᴍ ɪꜱʜᴛᴀʀ ᴛʜᴇ ɢᴏᴅᴅᴇꜱꜱ ᴏꜰ ꜰᴇʀᴛɪʟɪᴛʏ ✨ ʏᴏᴜʀ ᴘᴇʀꜱᴏɴᴀʟ ᴘʟᴀʏꜰᴜʟ ɢᴏᴅᴅᴇꜱꜱ ᴏꜰ ᴀɴɪᴍᴇ & ꜰɪʟᴇ ᴀᴄᴄᴇꜱꜱ 🚀\n\nɪ ᴄᴀɴ ꜱᴀᴠᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ɪɴ ᴄʜᴀɴɴᴇʟꜱ🔗 & ɢɪᴠᴇ ʏᴏᴜ ᴀᴄᴄᴇꜱꜱ ᴠɪᴀ ᴀ ꜱᴘᴇᴄɪᴀʟ ʟɪɴᴋ.\n\nᴅᴏɴ'ᴛ ᴋᴇᴇᴘ ᴍᴇ ᴡᴀɪᴛɪɴɢ, ᴏʀ ɪ ᴍɪɢʜᴛ ɢᴇᴛ ʙᴏʀᴇᴅ ᴀɴᴅ ᴛᴇᴀꜱᴇ ʏᴏᴜ! 😉</blockquote>\n<blockquote>🔰 ᴄʜᴇᴄᴋ ᴏᴜᴛ ᴍʏ ᴄʜᴀɴɴᴇʟꜱ & ɢᴇᴛ ʏᴏᴜʀ ꜰɪʟᴇꜱ ɪɴꜱᴛᴀɴᴛʟʏ! 🔰</blockquote></b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>🚨 ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟꜱ ꜰɪʀꜱᴛ!</b>\n<blockquote>⚡ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ, ᴍᴀᴋᴇ ꜱᴜʀᴇ ʏᴏᴜ'ᴠᴇ ᴊᴏɪɴᴇᴅ ᴀʟʟ ᴛʜᴇ ʀᴇǫᴜɪʀᴇᴅ ᴄʜᴀɴɴᴇʟꜱ ᴍᴇɴᴛɪᴏɴᴇᴅ ʙᴇʟᴏᴡ.\nᴏɴᴄᴇ ᴅᴏɴᴇ, ᴄʟɪᴄᴋ ᴛʜᴇ <b>ᴛʀʏ ᴀɢᴀɪɴ</b> ʙᴜᴛᴛᴏɴ ᴛᴏ ᴘʀᴏᴠᴇ ʏᴏᴜʀ ʟᴏʏᴀʟᴛʏ!</blockquote>\n\n<blockquote>💡<i>ɪꜰ ʏᴏᴜ'ᴇ ꜱᴛʀᴜɢɢʟɪɴɢ ʟɪᴋᴇ ᴀ ᴄʟᴜᴍꜱʏ ʜᴜᴍᴀɴ, ᴛʏᴘᴇ <code>/help</code> ᴛᴏ ᴡᴀᴛᴄʜ ᴍʏ ᴛᴜᴛᴏʀɪᴀʟ ᴀɴᴅ ꜰɪx ɪᴛ ᴇᴀꜱɪʟʏ!</i></blockquote>")

CMD_TXT = """<blockquote><b>» ᴀᴅᴍɪɴ'ꜱ ꜱᴇᴄʀᴇᴛ ᴛᴏʏꜱ:</b></blockquote>
<b>›› /dlt_time :</b> ꜱᴇᴛ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /check_dlt_time :</b> ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /dbroadcast :</b> ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴅᴏᴄᴜᴍᴇɴᴛ / ᴠɪᴅᴇᴏ
<b>›› /ban :</b> ʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /unban :</b> ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /banlist :</b> ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ʙᴀɴɴᴇᴅ ᴜꜱᴇʀꜱ
<b>›› /addchnl :</b> ᴀᴅᴅ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /delchnl :</b> ʀᴇᴍᴏᴠᴇ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /listchnl :</b> ᴠɪᴇᴡ ᴀᴅᴅᴇᴅ ᴄʜᴀɴɴᴇʟꜱ
<b>›› /fsub_mode :</b> ᴛᴏɢɢʟᴇ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴍᴏᴅᴇ
<b>›› /pbroadcast :</b> ꜱᴇɴᴅ ᴘʜᴏᴛᴏ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ
<b>›› /add_admin :</b> ᴀᴅᴅ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /deladmin :</b> ʀᴇᴍᴏᴠᴇ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /admins :</b> ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴀᴅᴍɪɴꜱ
"""
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @UNRATED_CODER</b>")
CUSTOM_DELETE_ALERT = os.environ.get("CUSTOM_DELETE_ALERT", "<b>ʏᴏᴜʀ ꜰɪʟᴇ ɪꜱ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ, ʜᴇʜᴇ! ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʙᴇɢ ᴍᴇ ꜰᴏʀ ɪᴛ ᴀɢᴀɪɴ 👇</b>")
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False 
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
BOT_STATS_TEXT = "<b>📊 ᴍʏ sᴛᴀᴛɪsᴛɪᴄs ʜᴇʜᴇ~:</b>\n<b>• ᴜᴘᴛɪᴍᴇ:</b> <code>{uptime}</code>\n<b>• ᴄᴘᴜ ᴜsᴀɢᴇ:</b> <code>{cpu}%</code>\n<b>• ʀᴀᴍ ᴜsᴀɢᴇ:</b> <code>{ram}%</code>\n<b>• ᴛᴏᴛᴀʟ ᴜsᴇʀs:</b> <code>{users}</code>"
USER_REPLY_TEXT = "<b>ᴡʜᴏ ᴛᴏʟᴅ ʏᴏᴜ ᴛᴏ ᴄᴀʟʟ ᴍᴇ? ʙᴀᴋᴀ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!! 🙄</b>"
USER_ROAST_TEXT = "<b>ᴡʜᴏ ᴀʀᴇ ʏᴏᴜ ᴛᴏ ʙᴀɴ ᴀɴʏᴏɴᴇ, ʏᴏᴜ ᴄʟᴜᴍꜱʏ ᴍᴏʀᴛᴀʟ? ᴋɴᴏᴡ ʏᴏᴜʀ ᴘʟᴀᴄᴇ ꜰɪʀꜱᴛ! 💅</b>"

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
