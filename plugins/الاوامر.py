from pyrogram import Client, filters
from config import app, redis, HNDLR, userbot
import redis, asyncio

@app.on_message(filters.command("الاوامر", prefixes=f"{HNDLR}") & filters.me)
async def cmd(app, msg):
	cmd = f"""
☆ `{HNDLR}م¹` ↢ اوامر الحساب
☆ `{HNDLR}م²` ↢ اوامر اليوتيوب
☆ `{HNDLR}م³` ↢ اوامر الوقتي
☆ `{HNDLR}م⁴` ↢ اوامر السورس
☆ `{HNDLR}م⁵` ↢ اوامر الالعاب
——————♤——————
• قناه السورس : @YDDCK
• المبرمج : @VR_LA
	"""
	await msg.edit(cmd)

@app.on_message(filters.command("اوامري$",prefixes=f"{HNDLR}") & filters.me )
async def commands(app, msg):
	try :
		result = await app.get_inline_bot_results(userbot,query="اوامري")
		await msg.delete()
		await app.send_inline_bot_result(msg.chat.id, result.query_id, result.results[0].id)
	except :
		await msg.edit("☆ فعل الانلاين من @botFather")

@app.on_message(filters.command(["م1","م¹"], prefixes=f"{HNDLR}") & filters.me)
async def help1(app, msg):
	help1 = f"""
☆ `م1` | اوامر الحساب
————————————

☆ `{HNDLR}انتحال` ↢ لانتحال اي حساب تريده
☆ `{HNDLR}رجوع` ↢ لاعاده الحساب كما كان

☆ `{HNDLR}ايدي` ↢ بالرد لعرض معلومات الحساب
☆ `{HNDLR}تليجراف` ↢ بالرد علي صوره لرفعها تليجراف
	"""
	await msg.edit(help1)
@app.on_message(filters.command(["م2","م²"], prefixes=f"{HNDLR}") & filters.me)
async def help2(app, msg):
	help2 = f"""
☆ `م2` | اوامر اليوتيوب
————————————

☆ `{HNDLR}بحث` ↢ للبحث في يوتيوب
☆ `{HNDLR}غ` ↢ لتحميل صوتي
☆ `{HNDLR}ف` ↢ لتحميل فيديو
	"""
	await msg.edit(help2)
@app.on_message(filters.command(["م3","م³"], prefixes=f"{HNDLR}") & filters.me)
async def help3(app, msg):
	help3 = f"""
☆ `م3` | اوامر الوقتي
————————————

☆ `{HNDLR}تفعيل الساعه` ↢ تفعيل ، تعطيل الاسم الوقتي
☆ `{HNDLR}تفعيل الصوره الوقتيه` ↢ تفعيل ، تعطيل الصوره الوقتيه
	"""
	await msg.edit(help3)
@app.on_message(filters.command(["م4","م⁴"], prefixes=f"{HNDLR}") & filters.me)
async def help4(app, msg):
	help4 = f"""
☆ `م4` | اوامر السورس
————————————

☆ `{HNDLR}بينج` ↢ لمعرفه سرعه السورس
☆ `{HNDLR}speedtest` ↢ سرعه الانترنت بالصوره

☆ `{HNDLR}سحب` ↢ سحب ملفات المواقع

☆ `{HNDLR}السورس` ↢ لعرض معلومات السورس
	"""
	await msg.edit(help4)

@app.on_message(filters.command(["م5","م⁵"], prefixes=f"{HNDLR}") & filters.me)
async def help5(app, msg):
	help5 = f"""
☆ `م5` | اوامر الالعاب
————————————

☆ `{HNDLR}اكس او` ↢ لعبه اكس او
☆ `{HNDLR}ريفرسي` ↢ لعبه ريفرسي
☆ `{HNDLR}حجره` ↢ لعبه حجره ورقه مقص
	"""
	await msg.edit(help5)
