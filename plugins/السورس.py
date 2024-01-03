from pyrogram import Client, filters
from config import app, HNDLR
import pyrogram, sys

pyro = pyrogram.__version__
py = sys.version

@app.on_message(filters.command(["سورس","السورس"], prefixes=f"{HNDLR}") & filters.me)
async def ping(app, msg):
	await msg.delete()
	txt = f"""
• المبرمج : @V_IRUuS
• قناه السورس : @YDDCK
• [pyrogram {pyro}](https://docs.pyrogram.org/)
• Python {py}
	"""
	await app.send_video(msg.chat.id,
	video="https://dev-media-uploader.pantheonsite.io/d_1agmiqd.mp4",
	caption=txt)