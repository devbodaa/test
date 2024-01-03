from pyrogram import Client, filters
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton)
from config import bot, SUDO_ID, HNDLR
import asyncio

reply_markup = InlineKeyboardMarkup([
	[InlineKeyboardButton("م¹",callback_data="help1"),InlineKeyboardButton("م²",callback_data="help2")],
	[InlineKeyboardButton("م³",callback_data="help3"),InlineKeyboardButton("م⁴",callback_data="help4")],
	[InlineKeyboardButton("م⁵",callback_data="help5")],
	[InlineKeyboardButton("🧑‍💻 Developer",url="https://t.me/V_IRUuS")]])

@bot.on_inline_query(filters.regex("^اوامري$"))
async def cmd(client, inline_query):
	await inline_query.answer(
		results=[
			InlineQueryResultArticle(
				title="الاوامر",
				input_message_content=InputTextMessageContent(f"☆ `{HNDLR}م¹` ↢ اوامر الحساب\n☆ `{HNDLR}م²` ↢ اوامر اليوتيوب\n☆ `{HNDLR}م³` ↢ اوامر الوقتي\n☆ `{HNDLR}م⁴` ↢ اوامر السورس\n☆ `{HNDLR}م⁵` ↢ اوامر الالعاب"),
				url="https://t.me/V_IRUuS",
				description="🧑‍💻 Developer",
				reply_markup=reply_markup
			),
		],
		cache_time=1
	)

help = f"""
☆ `{HNDLR}م¹` ↢ اوامر الحساب
☆ `{HNDLR}م²` ↢ اوامر اليوتيوب
☆ `{HNDLR}م³` ↢ اوامر الوقتي
☆ `{HNDLR}م⁴` ↢ اوامر السورس
☆ `{HNDLR}م⁵` ↢ اوامر الالعاب
"""

help1 = f"""
☆ `م1` | اوامر الحساب
————————————

☆ `{HNDLR}انتحال` ↢ لانتحال اي حساب تريده
☆ `{HNDLR}رجوع` ↢ لاعاده الحساب كما كان

☆ `{HNDLR}ايدي` ↢ بالرد لعرض معلومات الحساب
☆ `{HNDLR}تليجراف` ↢ بالرد علي صوره لرفعها تليجراف
"""

help2 = f"""
☆ `م2` | اوامر اليوتيوب
————————————

☆ `{HNDLR}بحث` ↢ للبحث في يوتيوب
☆ `{HNDLR}غ` ↢ لتحميل صوتي
☆ `{HNDLR}ف` ↢ لتحميل فيديو
"""

help3 = f"""
☆ `م3` | اوامر الوقتي
————————————

☆ `{HNDLR}تفعيل الساعه` ↢ تفعيل ، تعطيل الاسم الوقتي
☆ `{HNDLR}تفعيل الصوره الوقتيه` ↢ تفعيل ، تعطيل الصوره الوقتيه
"""

help4 = f"""
☆ `م4` | اوامر السورس
————————————

☆ `{HNDLR}بينج` ↢ لمعرفه سرعه السورس
☆ `{HNDLR}speedtest` ↢ سرعه الانترنت بالصوره

☆ `{HNDLR}سحب` ↢ سحب ملفات المواقع

☆ `{HNDLR}السورس` ↢ لعرض معلومات السورس
"""

help5 = f"""
☆ `م5` | اوامر الالعاب
————————————

☆ `{HNDLR}اكس او` ↢ لعبه اكس او
☆ `{HNDLR}ريفرسي` ↢ لعبه ريفرسي
☆ `{HNDLR}حجره` ↢ لعبه حجره ورقه مقص
"""

@bot.on_callback_query(filters.regex("^help1$") & filters.user(SUDO_ID))
async def m1(client, callback_query):
	await callback_query.edit_message_text(help1,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("☆ رجوع",callback_data="help")]]))
@bot.on_callback_query(filters.regex("^help2$") & filters.user(SUDO_ID))
async def m2(client, callback_query):
	await callback_query.edit_message_text(help2,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("☆ رجوع",callback_data="help")]]))
@bot.on_callback_query(filters.regex("^help3$") & filters.user(SUDO_ID))
async def m3(client, callback_query):
	await callback_query.edit_message_text(help3,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("☆ رجوع",callback_data="help")]]))
@bot.on_callback_query(filters.regex("^help4$") & filters.user(SUDO_ID))
async def m4(client, callback_query):
	await callback_query.edit_message_text(help4,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("☆ رجوع",callback_data="help")]]))
@bot.on_callback_query(filters.regex("^help5$") & filters.user(SUDO_ID))
async def m5(client, callback_query):
	await callback_query.edit_message_text(help5,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("☆ رجوع",callback_data="help")]]))
@bot.on_callback_query(filters.regex("^help$") & filters.user(SUDO_ID))
async def home(client, callback_query):
	await callback_query.edit_message_text(help,reply_markup=reply_markup)
