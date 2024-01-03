from pyrogram import Client, filters
from config import app, HNDLR, redis, SUDO_ID, timezone
from autoname import main as name
from autoname import profile
import time, os, asyncio
os.environ["TZ"] = timezone
time.tzset()

@app.on_message(filters.command("تعطيل الساعه$",prefixes=f"{HNDLR}") & filters.me)
async def clockk(c,msg):
	redis.delete(f"{SUDO_ID}clockk")
	get = await c.get_chat("me")
	await c.update_profile(first_name=f'{get.last_name}' ,last_name="")
	await msg.edit("• تم تعطيل الساعه")
@app.on_message(filters.command("تفعيل الساعه$",prefixes=f"{HNDLR}") & filters.me)
async def unclockk(c,msg):
	get = await c.get_chat("me")
	if get.last_name:
		my_name = f"{get.first_name} {get.last_name}"
	else :
		my_name = get.first_name
	redis.set(f"{SUDO_ID}clockk",my_name)
	await msg.edit("• تم تفعيل الساعه")
	await name()

@app.on_message(filters.command("تعطيل الصوره الوقتيه$",prefixes=f"{HNDLR}") & filters.me)
async def clock(c,msg):
	await msg.edit("• تم تعطيل الصوره الوقتيه")
	redis.delete(f"{SUDO_ID}clock")
@app.on_message(filters.command("تفعيل الصوره الوقتيه$",prefixes=f"{HNDLR}") & filters.me)
async def unclock(c,msg):
	await msg.edit("• تم تفعيل الصوره الوقتيه")
	redis.set(f"{SUDO_ID}clock","virus")
	await profile()
