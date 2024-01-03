# الكود واخده من @YYYBD , @FPFFG
from pyrogram import Client, filters, enums, idle
from asyncio import get_event_loop
from config import app, bot
from autoname import main as name
from autoname import profile
import asyncio

async def main():
	await app.start()
	await bot.start()
	try:
		await app.join_chat("YDDCJ")
		await app.join_chat("YDDCK")
		await app.join_chat("MaSPeRo_UpDaTe")
	except:
		pass
	await idle()
	await name()
	await profile()

print("VIRUS_USERBOT STARTED")
loop = get_event_loop()
loop.run_until_complete(main())