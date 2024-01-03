from pyrogram import Client, filters, enums
import redis, os

redis = redis.from_url(os.getenv("REDIS_URL"), decode_responses=True)

SUDO_ID = int(os.getenv("SUDO_ID", "5541009328"))
API_ID = int(os.getenv("API_ID", "9028013"))
API_HASH = os.getenv("API_HASH","cc894fc40424f9c8bbcf06b7355bd69d")
SESSION = os.getenv("SESSION")
TOKEN = os.getenv("TOKEN")
userbot = os.getenv("USERBOT")
HNDLR = os.getenv("HNDLR")
timezone = os.getenv("TIMEZONE")
app = Client("userbot",API_ID,API_HASH,in_memory=True,session_string=SESSION,plugins=dict(root="plugins"))
bot = Client("bot",API_ID,API_HASH,bot_token=TOKEN,in_memory=True,plugins=dict(root="plugins_bot"))
