#Recoded by @Its_Oreki_Hotarou

import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7622241172:AAHjInldlbjFXAADnL6FS97NV4_IuGzF-kM")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "27693340"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1056193e68c138ee16edc02578c559e1")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002413997036"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1718481517"))

#Port
PORT = os.environ.get("PORT", "8079")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://sagatobots00001:sagatobots100@cluster00001.vgdshkw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster00001")
DB_NAME = os.environ.get("DATABASE_NAME", "Fubuki_x_Robot_2_0_bot")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "0"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#pics
START_PIC = os.environ.get("START_PIC", "https://envs.sh/VNK.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/vXU.jpg")

#text
HELP_TXT = "<blockquote><b>Hi Dude!\n\nTo use this bot you just have to join both channels that's it..\nWatch Tutorial to open Link - <a href=https://t.me/+ZLu08PF-JUIzMjFl>Clickhere</a></b></blockquote>"

ABOUT_TXT = """<b>🤖 ᴍʏ ɴᴀᴍᴇ: {botname}

<b><blockquote expandable>» ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/Here_remo>Ꮢᴇᴍᴏ 🜲</a>
» ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href=https://t.me/play_tamil_dubbed_series>ᴘʟᴀʏ ᴄᴏᴍᴍᴜɴɪᴛʏ</a>
» ᴀᴅᴠᴀɴᴄᴇ ғᴇᴀᴛᴜʀᴇs: <a href=https://telegra.ph/BOT-FEATURES-11-09-28>Cʟɪᴄᴋ ʜᴇʀᴇ</a>
» ʟᴀɴɢᴜᴀɢᴇ: <a href=https://docs.python.org/3/>Pʏᴛʜᴏɴ 3</a>
» ʟɪʙʀᴀʀʏ: <a href=https://docs.pyrogram.org/>Pʏʀᴏɢʀᴀᴍ ᴠ2</a>
» ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=https://t.me/Here_remo>Ꮢᴇᴍᴏ</a></blockquote></b>"""

SHORT_MSG = "<b>⌯ ʏᴏᴜʀ ʟɪɴᴋ ɪꜱ ʀᴇᴀᴅʏ, ᴋɪɴᴅʟʏ ᴄʟɪᴄᴋ ᴏɴ ᴏᴘᴇɴ ʟɪɴᴋ ʙᴜᴛᴛᴏɴ..</b>"

#start message
START_MSG = os.environ.get("START_MESSAGE", """<b>⚡ ʏᴏ, {mention} ~  

<blockquote expandable>ʏᴏᴜ ᴡᴏᴋᴇ ᴍᴇ ᴜᴘ!\nʀᴇᴀᴅʏ ᴛᴏ ᴅɪᴠᴇ ɪɴᴛᴏ ꜱᴏᴍᴇ ᴄʜᴀᴏꜱ ᴀɴᴅ ɢʀᴀʙ ᴡʜᴀᴛ ʏᴏᴜ ɴᴇᴇᴅ?\n\nɴꜰɪʟᴇꜱ, ꜰᴜɴ ᴀɴᴅ ᴀ ᴡʜᴏʟᴇ ʟᴏᴛᴛᴀ ᴇɴᴇʀɢʏ—ʟᴇᴛ’ꜱ ʀᴏʟʟ!.</blockquote></b>""")

try:
    ADMINS = [1418213560]
    for x in (os.environ.get("ADMINS", "6587003349 7827448605 8160777407").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", """<b><blockquote>⚠️ Hᴇʏ, {mention} ×</blockquote>
Yᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴᴇᴅ {count}/{total} ᴄʜᴀɴɴᴇʟs ʏᴇᴛ. Pʟᴇᴀsᴇ ᴊᴏɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟs ᴘʀᴏᴠɪᴅᴇᴅ ʙᴇʟᴏᴡ, ᴛʜᴇɴ ᴛʀʏ ᴀɢᴀɪɴ.. !
</b>""")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

#Short Url or Api
SHORT_URL = os.environ.get("SHORTNER_URL", "https://gplinks.com")
SHORT_API = os.environ.get("SHORTNER_API", "fe8aa2557a758e856f79187ee1994a88da5dbd43")

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<blockquote>ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!</blockquote>"

AUTO_DEL = os.environ.get("AUTO_DEL", "True")
DEL_TIMER = int(os.environ.get("DEL_TIMER", "1800"))

# FIXED VERSION ↓↓↓
DEL_MSG = "(⚠️ Dᴜᴇ ᴛᴏ Cᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs....\n<blockquote>Yᴏᴜʀ ғɪʟᴇs ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ ᴡɪᴛʜɪɴ {}. Sᴏ ᴘʟᴇᴀsᴇ ғᴏʀᴡᴀʀᴅ ᴛʜᴇᴍ ᴛᴏ ᴀɴʏ ᴏᴛʜᴇʀ ᴘʟᴀᴄᴇ ғᴏʀ ғᴜᴛᴜʀᴇ ᴀᴠᴀɪʟᴀʙɪʟɪᴛʏ.</blockquote>)"

ADMINS.append(OWNER_ID)
ADMINS.append(1418213560)

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

#Bhen ke lavdo Credit hataya na ma choddunga wahi aakr salo use karo bas
